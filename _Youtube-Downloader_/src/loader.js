s = document.createElement("script");
s.src = chrome.extension.getURL("src/youtubedl.js");

s.onload = function(){
  this.remove();
}
document.head.appendChild(s);

// window.addEventListener("message", function(e){
//   console.log(e);
//   var ext = e.data.type.split("/")[1].split(";")[0];
//   var fn = e.data.name + '.' + ext;
//   console.log(fn);
//   chrome.runtime.sendMessage(e, function(res){
//     console.log(res);
//   });
  // chrome.downloads.download({url: e.data.url, filename: fn});
// });
