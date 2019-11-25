// this is the code which will be injected into a given page...

(function() {
    var videoURLs = window.ytplayer.config.args.url_encoded_fmt_stream_map.split(",").map(function(item) {
        return item.split("&").reduce(function(pre, cur) {
            console.log(pre, cur);
            cur = cur.split("=");
            return Object.assign(pre, {
                [cur[0]]: decodeURIComponent(cur[1])
            });
        }, {})
    });
    console.log("Our Extension has loaded", videoURLs);
})();