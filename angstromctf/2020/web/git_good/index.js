const express = require("express");
const fs = require("fs");
const path = require("path");
const app = express();

const port = process.env.PORT || 3000;
const flag = process.env.FLAG || "actf{placeholder_flag}";

// Inject the flag into the flag file if FLAG environment variable is set
if (process.env.FLAG) {
    try {
        fs.writeFileSync(path.join(__dirname, 'thisistheflag.txt'), flag);
        console.log('Flag injected successfully');
    } catch (error) {
        console.error('Error injecting flag:', error);
    }
}

app.use(express.static("."));

// Health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'healthy', timestamp: new Date().toISOString() });
});

app.listen(port, '0.0.0.0', function() {
    console.log(`App listening on port ${port}!`);
});
