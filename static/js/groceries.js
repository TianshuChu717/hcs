
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
                location.reload()

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
    
    const username = document.getElementById('username').value;
    console.log(username)
    $.ajax({
        type: 'GET',
        url: '/app/grids/',
        data:"username=" + username ,
        success: function(result){
            window.location = '/app/grids/'
            alert("We are going to help you find your password")
        },
    });
}