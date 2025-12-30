document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const idParam = urlParams.get('id');

    let finalId;
    if (idParam !== null && idParam !== "") {
        const parsedId = Number(idParam);

        if (!isNaN(parsedId) && parsedId >= 0 && parsedId <= 99) {
            finalId = Math.floor(parsedId);
        }
    }

    if (finalId === undefined) {
        finalId = Math.floor(Math.random() * 100);
    }

    generateProfile(finalId);
});


function generateProfile(id) {
	console.log(id)
	const profile = dataJSON.find(item => item.id === id);

	if (profile) {
		const templateBox = Handlebars.compile(
			document.getElementById('profile').innerHTML
		);

		document.getElementById('profile').innerHTML = templateBox({
			dataProfile: profile,
		});
	} else {
		console.error("Perfil não encontrado no banco de dados.");
	}
}

Handlebars.registerHelper('inc', function(value) {
    return parseInt(value) + 1;
});


function reloadPage(){
	window.location.reload();
}

function toggleView(isChecked){
	document.getElementById("answer").classList.toggle("d-none")
}