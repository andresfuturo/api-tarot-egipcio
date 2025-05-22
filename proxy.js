const httpProxy = require('http-proxy');
const http = require('http');

const proxy = httpProxy.createProxyServer({});

const server = http.createServer((req, res) => {
    if (req.url.startsWith('/api/cartas-egipcias')) {
        proxy.web(req, res, { target: 'http://127.0.0.1:8000' });
    } else {
        res.writeHead(404);
        res.end('Not found');
    }
});

server.listen(8001, () => {
    console.log('Proxy server running on port 8001');
});
