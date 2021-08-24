

// document.addEventListener('click', funciont (event) {
//     if(event.target && event.target.nodeName == 'BUTTON') {
//         event.targe; //  就是这个家伙点的，你要对它做什么就写这里.
//     }
// })

$("input[type='button']").bind('click',function() { alert("11"); });
$("button").bind('click',function() { alert("11"); });

// <script>
// 	document.onclick = function(){
// 		var obj = event.srcElement;
// 		if (obj.type == "button"){
// 			alert(obj,id)
// 		}
// 	}
// </script>