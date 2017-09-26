$(function(){
	let nav=$('<div class="col-md-2" id="nav"><div id="navBox" class="list-group"></div></div>')
	nav.css({
		    position: 'fixed',
		    top: '50px',
		    left: '-210px'
		})
	$('body').prepend(nav)
	let content = $('.content');
	let h2s = content.find('h2')
	let h3s = content.find('h3')
	let h4s = content.find('h4')
	let hs=[]
	let navBox = $('#navBox')
	let width = parseInt(navBox.css("width"))
	let step=4;
	h2s.each(function(i,h){
		h = $(h);
		hs.push({weight:2,
			top:h.position().top,
			id:h.attr('id'),
			text:h.text()
		})
	})
	h3s.each(function(i,h){
		h = $(h);
		hs.push({weight:3,
			top:h.position().top,
			id:h.attr('id'),
			text:h.text()
		})
	})
	h4s.each(function(i,h){
		h = $(h);
		hs.push({weight:4,
			top:h.position().top,
			id:h.attr('id'),
			text:h.text()
		})
	})

	hs.sort(function(a, b){
		return a.top - b.top
	})
	hs.forEach(function(obj){
		link = '<a class="list-group-item list-group-item-action" href="#'+ obj.id +'">'+ obj.text +'</a>'
		let indentation=step * (obj.weight-2)
		let w = width - indentation
		link = $(link).css({left:indentation + 'px', width:w + 'px'})
		navBox.append(link)
	})
	$('body').scrollspy({ target: '#navBox' })
	navBox.find('a.list-group-item').css({
		'background-color': 'rgb(26, 83, 100)'
	})

	nav.hover(function(){
		console.log(nav)
		console.log(nav.animate)
		nav.css({left:'0px'})
	},function(){
		nav.css({left:'-210px'})
	})
	$(window).resize(function(){
		if($(window).width()<629){
			nav.hide()
		}else{
			nav.show()
		}
	})
})