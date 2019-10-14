// this is the code which will be injected into a given page...

(function() {
	function trim(x) {
		return x.replace(/^\s+|\s+$/g, '');
	}

	var css_ = window.prompt('Enter the css selector for the elements to be scrapped')
	var att_ = window.prompt('Enter the attribute to be scrapped', 'text').split(',')
	var att_ = att_.map(trim)
	console.log(att_)

	var elems = document.querySelectorAll(css_)
	console.log('query selected')
	tablecontent = '<table style="width:100%;;" border="1"><tr><td>Iteration</td><td>Data</td></tr>'
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
	tablecontent += '</table>'
	console.log(tablecontent)
	var win = window.open("", "Title", "width=780,height=200");
	win.document.body.innerHTML = tablecontent;
})();
