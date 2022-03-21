
function add(name){
    // const good = $('#name').val();

    const good =name

    $.ajax({
        type: 'POST',
        url: '/app/add_like/',
        data:"good=" + good ,
        success: function(result){
            console.log(result)
            if(result==2){
                alert("??")
            }
            else if(result==1){
                alert("succesfully added");
            }
            else{
                alert("error happened");
            }
        },
        error: function(result){
            message("error")
        }
    });
};