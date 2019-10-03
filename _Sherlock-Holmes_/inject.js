// this is the code which will be injected into a given page...

(function() {
	function trim(x) {
		return x.replace(/^\s+|\s+$/g, '');
	}

	var div = document.createElement('div');
	div.style.position = 'fixed';
	div.style.top = 0;
	div.style.right = 0;
	div.innerHTML = '<h1>Access Obtained!</h1>';
	div.style.boxShadow = "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)";
	div.style.height = "200px";
	div.style.width = "500px";
	div.style.backgroundColor = "#fff";
	div.style.overflowY = "scroll";
	div.style.overflowX = "scroll";
	div.style.textAlign = "center";
	div.style.fontFamily = "Courier New, monospace"
	div.style.zIndex = "100000";
	document.body.appendChild(div);

	div.innerHTML += '<table style="width:100%;;" border="1"><tr><td>Iteration</td><td>Data</td></tr></table>'
	table = div.lastChild
	table.style.border = "1px solid #000000";

	var css_ = window.prompt('Enter the css selector for the elements to be scrapped')
	var att_ = window.prompt('Enter the attribute to be scrapped', 'text').split(',')
	var att_ = att_.map(trim)
	console.log(att_)

	var elems = document.querySelectorAll(css_)
	console.log('query selected')
	tablecontent = ''
	for(var i=0; i<elems.length; i++)
	{
		tablecontent += '<tr><td>'+i+'</td>'
		for(var j=0; j<att_.length; j++)
		{
			if(att_[j] == 'text')
				tablecontent += '<td>'+elems[i].innerHTML+'</td>'
			else
				tablecontent += '<td>'+elems[i].getAttribute(att_[j])+'</td>'
		}
		tablecontent += '</tr>'
	}
	table.innerHTML = tablecontent
	console.log(tablecontent)
	var btn = document.createElement('button');
	btn.style.position = 'fixed';
	btn.style.top = 0;
	btn.style.right = 0;
	btn.innerHTML = 'X';
	btn.style.zIndex = "100001";
	document.body.appendChild(btn);
	btn.onclick = function(){
		div.style.display = "none";
		btn.style.display = "none"
	};
})();
