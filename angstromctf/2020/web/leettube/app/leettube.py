#!/usr/bin/env python
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import os

# Get flag from environment variable, default to placeholder
flag = os.environ.get('FLAG', 'actf{fake_flag_placeholder_for_testing}')

videos = []
for file in os.listdir('videos'):
	os.chmod('videos/'+file, 0o600)
	content = open('videos/'+file, 'rb').read()
	
	# If this is the flag video, inject the flag
	if file.startswith('UNPUBLISHED_Flag'):
		# Replace placeholder with actual flag in the video content
		placeholder = b'PLACEHOLDER_FLAG_HERE'
		if placeholder in content:
			content = content.replace(placeholder, flag.encode('utf-8'))
		else:
			# If no placeholder found, append flag as metadata comment
			# This is a simple approach - in a real scenario you might embed it properly
			content = content + b'\n<!-- FLAG: ' + flag.encode('utf-8') + b' -->\n'
	
	videos.append({'title': file.split('.')[0], 'path': 'videos/'+file, 'content': content})

published = []
for video in videos:
	if video['title'].startswith('UNPUBLISHED'): os.chmod(video['path'], 0) # make sure you can't just guess the filename
	else: published.append(video)

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			self.path = urllib.parse.unquote(self.path)
			if self.path.startswith('/videos/'):
				file = os.path.abspath('.'+self.path)
				# Find the matching video in our processed videos list
				video_obj = None
				for v in videos:
					if os.path.abspath(v['path']) == file:
						video_obj = v
						break
			
				if not video_obj:
					self.send_response(404)
					self.end_headers()
					return
				
				reqrange = self.headers.get('Range', 'bytes 0-')
				ranges = list(int(i) for i in reqrange[6:].split('-') if i)
				if len(ranges) == 1: ranges.append(ranges[0]+65536)
			
				try:
					full_content = video_obj['content']
					if ranges[0] >= len(full_content):
						self.send_response(416)  # Range not satisfiable
						self.end_headers()
						return
				
					end_byte = min(ranges[1], len(full_content) - 1)
					content = full_content[ranges[0]:end_byte + 1]
				
					self.send_response(206)
					self.send_header('Accept-Ranges', 'bytes')
					self.send_header('Content-Type', 'video/mp4')
					self.send_header('Content-Range', 'bytes '+str(ranges[0])+'-'+str(ranges[0]+len(content)-1)+'/'+str(len(full_content)))
					self.end_headers()
					self.wfile.write(content)
				except Exception as e:
					self.send_response(404)
					self.end_headers()
					return
			elif self.path == '/':
				self.send_response(200)
				self.send_header('Content-Type', 'text/html')
				self.end_headers()
				self.wfile.write(("""
<style>
body {
	background-color: black;
	color: #00e33d;
	font-family: monospace;
	max-width: 30em;
	font-size: 1.5em;
	margin: 2em auto;
}
</style>
<h1>LeetTube</h1>
<p>There are <strong>"""+str(len(published))+"</strong> published video"+('s' if len(published) > 1 else '')+" and <strong>"+str(len(videos)-len(published))+"</strong> unpublished video"+('s' if len(videos)-len(published) > 1 else '')+".</p>"+''.join("<h2>"+video["title"]+"</h2><video controls src=\""+video["path"]+"\"></video>" for video in published)).encode('utf-8'))
			else:
				self.send_response(404)
				self.end_headers()
		except:
			self.send_response(500)
			self.end_headers()

httpd = HTTPServer(('', 8000), RequestHandler)
httpd.serve_forever()
