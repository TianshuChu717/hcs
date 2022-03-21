
function add(name){
    // const good = $('#name').val();

    const good =name
    console.log("Adding grocery:",name)
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

function generate_grid(){
    
    const username = document.getElementById('')
    console.log("username",username)
    $.ajax({
        type: 'GET',
        url: '/app/grids/',
        data:"username=" + username ,
        success: function(result){
            console.log(result)
            // if(result==2){
            //     alert("??")
            // }
            // else if(result==1){
            //     alert("succesfully added");
            // }
            // else{
            //     alert("error happened");
            // }
        },
        error: function(result){
            // message("error")
        }
    });
}