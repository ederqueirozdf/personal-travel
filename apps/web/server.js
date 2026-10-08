const express = require('express');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send(`
    <html>
      <head>
        <title>Travel Agent</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 40px; background: #f4f7fb; }
          .card { max-width: 800px; margin: 0 auto; background: white; border-radius: 12px; padding: 32px; box-shadow: 0 8px 24px rgba(0,0,0,0.08); }
          h1 { color: #123; }
          p { color: #466; }
          ul { color: #466; }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>Travel Agent MVP</h1>
          <p>System ready for flight searches in cash and miles.</p>
          <ul>
            <li>Search by origin and destination</li>
            <li>Flexible date window analysis</li>
            <li>Comparison with miles and cash</li>
            <li>Top 3 recommendations</li>
          </ul>
        </div>
      </body>
    </html>
  `);
});

app.listen(port, () => {
  console.log(`Frontend running on port ${port}`);
});
