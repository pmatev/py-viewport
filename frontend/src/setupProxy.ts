const { createProxyMiddleware } = require('http-proxy-middleware');

const socketProxy = ;

module.exports = function(app: any) {
    app.use('/viewport', createProxyMiddleware({
        target: 'http://localhost:3000/viewport',
        ws: true,
    }));
};

export {}