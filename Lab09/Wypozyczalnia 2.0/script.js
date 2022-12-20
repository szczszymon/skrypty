var vehicleState = [2, 4, 1];

var vehicleBanned = [false, false, false];

var vehicleInfo = [
    [[`<div class="card mb-3">
        <div class="row g-0">
            <div class="col-md-4">
                <img src="Pictures/hiland.jpg" class="img-fluid rounded-start m-sm-0 m-md-2" alt="hiland">
            </div>

            <div class="col-md-8">
                <div class="card-body" id="vehInfo">
                    <h2 class="card-title">Rower wyścigowy Hiland</h2>
                    <p class="card-text">Ten rower ma wysokiej jakości ultralekką aluminiową ramę i wewnętrzną konstrukcję z drutu. Układ hamulcowy składa się z podwójnych hamulców zaciskowych. 3 x 7-biegowa dźwignia zmiany biegów Shimano zapewnia pełną kontrolę w każdej sytuacji. </p>
                    <p class="card-text"><b id="shForm2" style="cursor: pointer;" data-bs-toggle="offcanvas" data-bs-target="#offForm2" aria-controls="offForm2" onclick="document.getElementById('vehID').value = 0;">Liczba dostępnych sztuk: `],
        [`</b></p>
                    <p class="card-text"><b>Cena zakupu: 1399 PLN</b></p>
                    <p class="card-text"><b>Cena wypożyczenia: 3 PLN /min</b></p>
                </div>
            </div>
        </div>
    </div>`]],

    [[`<div class="card mb-3">
        <div class="row g-0">
            <div class="col-md-4">
                <img src="Pictures/indiana.jpg" class="img-fluid rounded-start m-sm-0 m-md-2" alt="indiana">
            </div>

            <div class="col-md-8">
                <div class="card-body" id="vehInfo">
                    <h2 class="card-title">Rower górski Indiana</h2>
                    <p class="card-text">Rower przeznaczony do jazdy po bardzo wymagającym terenie. Świetnie sprawdzi się zarówno podczas jazdy po górzystych bezdrożach, popołudniowych przejażdżek, jak i codziennych wypraw. Szczególnie dobrze sprawdzi się podczas jazdy po kamienistych ścieżkach i stromych wzniesieniach. Dzięki dużemu rozmiarowi kół pokonywanie przeszkód na tym rowerze jest prostsze.</p>
                    <p class="card-text"><b id="shForm2" style="cursor: pointer;" data-bs-toggle="offcanvas" data-bs-target="#offForm2" aria-controls="offForm2" onclick="document.getElementById('vehID').value = 1;">Liczba dostępnych sztuk: `],
        [`</b></p>
                    <p class="card-text"><b>Cena zakupu: 1199 PLN</b></p>
                    <p class="card-text"><b>Cena wypożyczenia: 3 PLN /min</b></p>
                </div>
            </div>
        </div>
    </div>`]],

    [[`<div class="card mb-3">
        <div class="row g-0">
            <div class="col-md-4">
                <img src="Pictures/scooter.jpg" class="img-fluid rounded-start m-sm-0 m-md-2" alt="jivr">
            </div>

            <div class="col-md-8">
                <div class="card-body" id="vehInfo">
                    <h2 class="card-title">Hulajnoga elektryczna JIVR</h2>
                    <p class="card-text">JIVR Scooter to lekka, składana hulajnoga elektryczna, która świetnie sprawdzi się podczas jazdy po mieście i nie tylko. Łatwo wyjmowany litowo-jonowy akumulator zapewnia zasięg sięgający nawet 50 kilometrów. Opatentowany układ kierowniczy zapewnia doskonałą stabilność i większą kontrolę na drodze, zapewniając doskonałe wrażenia z jazdy.</p>
                    <p class="card-text"><b id="shForm2" style="cursor: pointer;" data-bs-toggle="offcanvas" data-bs-target="#offForm2" aria-controls="offForm2" onclick="document.getElementById('vehID').value = 2;">Liczba dostępnych sztuk: `],
        [`</b></p>
                    <p class="card-text"><b>Cena zakupu: 1299 PLN</b></p>
                    <p class="card-text"><b>Cena wypożyczenia: 3 PLN /min</b></p>
                </div>
            </div>
        </div>
    </div>`]],

    [[`<div class="card mb-3">
        <div class="row g-0">
            <div class="col-md-4">
                <img src="Pictures/hiland.jpg" class="img-fluid rounded-start m-sm-0 m-md-2" alt="hiland">
            </div>

            <div class="col-md-8">
                <div class="card-body text-muted text-decoration-line-through" id="vehInfo">
                    <h2 class="card-title">Rower wyścigowy Hiland</h2>
                    <p class="card-text">Ten rower ma wysokiej jakości ultralekką aluminiową ramę i wewnętrzną konstrukcję z drutu. Układ hamulcowy składa się z podwójnych hamulców zaciskowych. 3 x 7-biegowa dźwignia zmiany biegów Shimano zapewnia pełną kontrolę w każdej sytuacji. </p>
                    <p class="card-text"><b id="shForm2" style="cursor: pointer;" data-bs-toggle="offcanvas" data-bs-target="#offForm2" aria-controls="offForm2" onclick="document.getElementById('vehID').value = 0;">Liczba dostępnych sztuk: `],
        [`</b></p>
                    <p class="card-text"><b>Cena zakupu: 1399 PLN</b></p>
                    <p class="card-text"><b>Cena wypożyczenia: 3 PLN /min</b></p>
                </div>
            </div>
        </div>
    </div>`]],

    [[`<div class="card mb-3">
        <div class="row g-0">
            <div class="col-md-4">
                <img src="Pictures/indiana.jpg" class="img-fluid rounded-start m-sm-0 m-md-2" alt="indiana">
            </div>

            <div class="col-md-8">
                <div class="card-body text-muted text-decoration-line-through" id="vehInfo">
                    <h2 class="card-title">Rower górski Indiana</h2>
                    <p class="card-text">Rower przeznaczony do jazdy po bardzo wymagającym terenie. Świetnie sprawdzi się zarówno podczas jazdy po górzystych bezdrożach, popołudniowych przejażdżek, jak i codziennych wypraw. Szczególnie dobrze sprawdzi się podczas jazdy po kamienistych ścieżkach i stromych wzniesieniach. Dzięki dużemu rozmiarowi kół pokonywanie przeszkód na tym rowerze jest prostsze.</p>
                    <p class="card-text"><b id="shForm2" style="cursor: pointer;" data-bs-toggle="offcanvas" data-bs-target="#offForm2" aria-controls="offForm2" onclick="document.getElementById('vehID').value = 1;">Liczba dostępnych sztuk: `],
        [`</b></p>
                    <p class="card-text"><b>Cena zakupu: 1199 PLN</b></p>
                    <p class="card-text"><b>Cena wypożyczenia: 3 PLN /min</b></p>
                </div>
            </div>
        </div>
    </div>`]],

    [[`<div class="card mb-3">
        <div class="row g-0">
            <div class="col-md-4">
                <img src="Pictures/scooter.jpg" class="img-fluid rounded-start m-sm-0 m-md-2" alt="jivr">
            </div>

            <div class="col-md-8">
                <div class="card-body text-muted text-decoration-line-through" id="vehInfo">
                    <h2 class="card-title">Hulajnoga elektryczna JIVR</h2>
                    <p class="card-text">JIVR Scooter to lekka, składana hulajnoga elektryczna, która świetnie sprawdzi się podczas jazdy po mieście i nie tylko. Łatwo wyjmowany litowo-jonowy akumulator zapewnia zasięg sięgający nawet 50 kilometrów. Opatentowany układ kierowniczy zapewnia doskonałą stabilność i większą kontrolę na drodze, zapewniając doskonałe wrażenia z jazdy.</p>
                    <p class="card-text"><b id="shForm2" style="cursor: pointer;" data-bs-toggle="offcanvas" data-bs-target="#offForm2" aria-controls="offForm2" onclick="document.getElementById('vehID').value = 2;">Liczba dostępnych sztuk: `],
    [`</b></p>
                    <p class="card-text"><b>Cena zakupu: 1299 PLN</b></p>
                    <p class="card-text"><b>Cena wypożyczenia: 3 PLN /min</b></p>
                </div>
            </div>
        </div>
    </div>`]]
];

var defVehicleCard = `<div class="col" style="cursor: pointer;" onclick="ret(`;
var vehicleCard = [`);">
                        <div class="card h-60">
                            <img src="Pictures/hiland.jpg" class="card-img-top" alt="hiland">
                            <div class="card-body bg-dark text-white">
                                <h5 class="card-title">Rower wyścigowy Hiland</h5>
                            </div>
                        </div>
                    </div>`,

    `);">
        <div class="card h-60">
            <img src="Pictures/indiana.jpg" class="card-img-top" alt="indiana">
            <div class="card-body bg-dark text-white">
                <h5 class="card-title">Rower górski Indiana</h5>
            </div>
        </div>
    </div>`,

    `);">
        <div class="card h-60">
            <img src="Pictures/scooter.jpg" class="card-img-top" alt="jivr">
            <div class="card-body bg-dark text-white">
                <h5 class="card-title">Hulajnoga elektryczna JIVR</h5>
            </div>
        </div>
    </div>`
];

var currentId = 0;
var nV = 3;
var borrowers = {"MarzenaNowak":[1, 0, 1], "JanKowalski":[1, 1, 1], "AnnaChmiel":[0, 1, 0]}
var people = ["MarzenaNowak", "JanKowalski", "AnnaChmiel"];

function change(id){
    if (vehicleBanned[id] === true)
        document.getElementById("vehicleInfo").innerHTML = vehicleInfo[id + nV][0] + vehicleState[id] + vehicleInfo[id + nV][1];
    else
        document.getElementById("vehicleInfo").innerHTML = vehicleInfo[id][0] + vehicleState[id] + vehicleInfo[id][1];

    currentId = id;
}// change()

function add(){
    var vname = document.getElementById("vnameInput").value;
    var desc = document.getElementById("descInput").value;
    var pic = document.getElementById('picInput').value;
    var quantity = document.getElementById("quanInput").value;
    var price = document.getElementById("priceInput").value;
    var borrow = document.getElementById('borrowInput').value;

    if (vname === "" || desc === "" || pic === "" || quantity === "" || price === "" || borrow === "")
        return;

    document.getElementById("vnameInput").value = "";
    document.getElementById("descInput").value = "";
    document.getElementById('picInput').value = "";
    document.getElementById("quanInput").value = "";
    document.getElementById("priceInput").value = "";
    document.getElementById('borrowInput').value = "";

    for (let i = 0; i < people.length; i++) {
        borrowers[people[i]].push(0);
    }// for

    vehicleState.push(parseInt(quantity));

    if (parseInt(quantity) <= 0)
        vehicleBanned.push(true);
    else
        vehicleBanned.push(false);

    vehicleInfo.splice(nV, 0, [[`<div class="card mb-3">
                                                    <div class="row g-0">
                                                        <div class="col-md-4">
                                                            <img src="Pictures/` + pic + `.jpg" class="img-fluid rounded-start m-sm-0 m-md-2" alt="` + pic + `">
                                                        </div>
                                            
                                                        <div class="col-md-8">
                                                            <div class="card-body" id="vehInfo">
                                                                <h2 class="card-title">` + vname + `</h2>
                                                                <p class="card-text">` + desc + `</p>
                                                                <p class="card-text"><b id="shForm2" style="cursor: pointer;" data-bs-toggle="offcanvas" data-bs-target="#offForm2" aria-controls="offForm2" onclick="document.getElementById('vehID').value = ` + nV + `;">Liczba dostępnych sztuk: `],
                                                    [`</b></p>
                                                                <p class="card-text"><b>Cena zakupu: ` + price + ` PLN</b></p>
                                                                <p class="card-text"><b>Cena wypożyczenia: ` + borrow + ` PLN /min</b></p>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>`]]);

    vehicleInfo.push([[`<div class="card mb-3">
                            <div class="row g-0">
                                <div class="col-md-4">
                                    <img src="Pictures/` + pic + `.jpg" class="img-fluid rounded-start m-sm-0 m-md-2" alt="` + pic + `">
                                </div>
                    
                                <div class="col-md-8">
                                    <div class="card-body text-muted text-decoration-line-through" id="vehInfo">
                                        <h2 class="card-title">` + vname + `</h2>
                                        <p class="card-text">` + desc + `</p>
                                        <p class="card-text"><b id="shForm2" style="cursor: pointer;" data-bs-toggle="offcanvas" data-bs-target="#offForm2" aria-controls="offForm2" onclick="document.getElementById('vehID').value = ` + nV + `;">Liczba dostępnych sztuk: `],
                            [`</b></p>
                                        <p class="card-text"><b>Cena zakupu: ` + price + ` PLN</b></p>
                                        <p class="card-text"><b>Cena wypożyczenia: ` + borrow + ` PLN /min</b></p>
                                    </div>
                                </div>
                            </div>
                        </div>`]]);

    vehicleCard.push(`);">
                    <div class="card h-60">
                        <img src="Pictures/` + pic + `.jpg" class="card-img-top" alt="` + pic + `">
                        <div class="card-body bg-dark text-white">
                            <h5 class="card-title">` + vname + `</h5>
                        </div>
                    </div>
                </div>`);

    document.getElementById("vehNames").innerHTML += `<button type="button" class="btn btn-dark" onclick="change(` + nV + `)">` + vname + `</button>`;
    nV++;


}// add()

function borrow(){
    var name = document.getElementById("nameInput").value;
    var surname = document.getElementById("surnameInput").value;
    var vehicle = document.getElementById('vehID').value;

    document.getElementById('nameInput').value = "";
    document.getElementById('surnameInput').value = "";

    if (vehicleState[vehicle] === 1) {
        document.getElementById("vehInfo").classList.add("text-muted");
        document.getElementById("vehInfo").classList.add("text-decoration-line-through");
        document.getElementById("shForm2").classList.add("disabled");
        vehicleBanned[vehicle] = true;
    }// if

    vehicleState[vehicle]--;
    borrowers[name + surname][vehicle]++;

    change(currentId);
    generateBorrowers();
}// borrow()

function ret(name, vehicle){
    borrowers[people[name]][vehicle]--;

    if (vehicleState[vehicle] === 0) {
        document.getElementById("vehInfo").classList.remove("text-muted");
        document.getElementById("vehInfo").classList.remove("text-decoration-line-through");
        document.getElementById("shForm2").classList.remove("disabled");
        vehicleBanned[vehicle] = false;
    }// if

    vehicleState[vehicle]++;

    change(currentId);
    generateBorrowers();
}// ret()

function generateBorrowers(){
    for (let n = 0; n < people.length; n++) {
        document.getElementById(people[n]).innerHTML = "";

        for (let i = 0; i < borrowers[people[n]].length; i++) {
            for (let j = 0; j < borrowers[people[n]][i]; j++) {
                document.getElementById(people[n]).innerHTML += (defVehicleCard + n + ", " + i + vehicleCard[i]);
            }// for content
        }// for vehicle
    }// for name
}// generateBorrowers()
