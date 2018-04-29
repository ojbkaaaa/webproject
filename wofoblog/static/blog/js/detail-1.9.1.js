 /*用于获取评论和回复并发送到后台
 */

    function subcom(nid){
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        var number_commit = nid
        var blog_commit=CKEDITOR.instances.editor1.getData();
        console.log(number_commit)
        console.log(blog_commit)
         $.ajax({
                url:"/comments/comment",
                type:'POST',
                dataType:'json',
                cache: false,
                async:true,

                traditional: true,
                data:{
                'csrfmiddlewaretoken': csrf,
                "number_commit":number_commit,
                "blog_commit":blog_commit,

                },
                success:function(e){
                    alert(e);
                    window.location.reload();
                }

            })

    };



    function mm(nid){
		var class_id = document.getElementById(nid);
		var class_list = class_id.nextSibling.nextSibling;
        var forms = $('ul form')
        for(var i=0;i<forms.length;i++){
            forms[i].classList.add('hidden');}
        class_list.classList.remove('hidden');

        };
    function gg(nid){
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        var class_id = document.getElementsByClassName(nid);
        class_id[0].classList.add('hidden');
        var number = $('.tm-blog-post').attr('id');
        var arr = number.split('/');
        var number = arr[1];   
        blog_commit = class_id[0].childNodes[1].value;
        console.log(blog_commit);


        number_commit=nid;
        to_blog_id=number;

        $.ajax({
                url:"/comments/add",
                type:'POST',
                dataType:'json',
                cache: false,
                async:true,
                traditional: true,
                data:{
                'csrfmiddlewaretoken': csrf,
                "number_commit":nid,
                "to_blog_id":number,
                "blog_commit":blog_commit

                },
                success:function(e){
                    alert(e);
                    window.location.reload();
                }
            })
    }

