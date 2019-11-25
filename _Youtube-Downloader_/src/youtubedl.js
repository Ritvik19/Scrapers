function downloadVideo(){
  console.log("download this video");
  var dl = document.getElementById("videoDownloadDropdown");
  if(dl.className.indexOf("shown") > -1){
    dl.className = dl.className.replace("shown", "")
  }
  else{
    dl.className += " shown";
  }
  // var data = {"type": "download clicked"};
  // window.postMessage(data, "*");
}

// function downloadURI(event){
//   event.preventDefault();
//
//   var url = event.currentTarget.getAttribute("href");
//   var name = document.getElementsByTagName("title")[0].innerText;
//   var datatype = event.currentTarget.getAttribute("data-type");
//   var data = {url: url, name: name, sender: "YTDL", type: datatype};
//   window.postMessage(data, "*");
// }

var videoURLs = window.ytplayer.config.args.url_encoded_fmt_stream_map.split(",").map(function(item){
  return item.split("&").reduce(function(pre, cur){
    console.log(pre, cur);
    cur = cur.split("=");
    return Object.assign(pre, {[cur[0]]: decodeURIComponent(cur[1])});
  }, {})
});
console.log("Our Extension has loaded", videoURLs);

// var container = document.getElementsByClassName("style-scope ytd-video-primary-info-renderer")[0];
var container = document.getElementById("info");

var btn = document.createElement("button");
btn.className = "dwnld";
btn.setAttribute("role", "button");
btn.innerText = "Download";
container.appendChild(btn);
btn.addEventListener("click", downloadVideo);

var dropdown = document.createElement("div")
dropdown.id = "videoDownloadDropdown";
container.appendChild(dropdown);

var dropList = document.createElement("ul");
dropdown.appendChild(dropList);

for (var i in videoURLs) {
  var item = document.createElement("a");
  item.innerText = videoURLs[i]["quality"];
  item.setAttribute("href", videoURLs[i]["url"]);
  item.setAttribute("target", "_blank");
  // item.setAttribute("data-type", videoURLs[i]["type"])
  // item.addEventListener("click", downloadURI)
  dropList.appendChild(item);
}
