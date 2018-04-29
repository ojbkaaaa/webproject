/*
用于个人中心新增博文
*/


  function click_jojo(nid){
		var class_id = document.getElementById(nid);
		var class_list = class_id.parentElement.children;
		for(var i=0;i<class_list.length;i++){
                var current_item = class_list[i];
                current_item.className='chose hidden';
            }
        class_id.className='chose';}

 $(document).ready(function(){
        $('#add').click(function(){
            var t = $('#title').val();
            var item = {
                    "title":$('#title').val(),
                    "blog_tag":$('#blog_tag').val(),
                    "blog_content":$('#blog_content').val()}
            console.log(t);
            $.ajax({
                url:"/blog/user_info",
                headers:{ "X-CSRFtoken":$.cookie("csrftoken")},
                type:'POST',
                dataType:'json',
                async:true,
                data:JSON.stringify(item),
                success:function(e){
                    alert(e)
                }
            })
        })
  })

