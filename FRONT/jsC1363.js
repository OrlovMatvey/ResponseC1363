function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split('; ');
        for (let i = 0; i < cookies.length+1; i++) {
            const cookie = (cookies[i]);
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken')
console.log(csrftoken)

function GetSolution(){
    if (isNaN(document.getElementById('iter'))!=True &
        isNaN(document.getElementById('count'))!=True &
        isNaN(document.getElementById('special'))!=True &
        length(document.getElementById('nodes'))>=(n-1)*3
    ){
    fetch('http://127.0.0.1:8000/task', {
        method: 'POST',
        credentials: "include",
        headers: {'X-CSRFToken': csrftoken},
        body: JSON.stringify({
            't': document.getElementById('iter'),
            'n': document.getElementById('count'), 
            'x': document.getElementById('special'), 
            'uv': document.getElementById('nodes'),
            "csrftoken": csrftoken
        })
    })
}
}