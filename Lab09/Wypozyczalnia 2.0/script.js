var vehicles = [
    `<div class="card mb-3">
                        <div class="row g-0">
                            <div class="col-md-4">
                                <img src="Pictures/hiland.jpg" class="img-fluid rounded-start m-sm-0 m-md-2" alt="hiland">
                            </div>

                            <div class="col-md-8">
                                <div class="card-body">
                                    <h2 class="card-title">Rower górski Hiland</h2>
                                    <p class="card-text">Tekst o rowerze hiland / stan</p>
                                    <p class="card-text"><b>Cena zakupu: 1200 PLN</b></p>
                                    <p class="card-text"><b>Cena wypożyczenia: 3 PLN /min</b></p>
                                </div>
                            </div>
                        </div>
                    </div>`,

    `<div class="card mb-3">
                        <div class="row g-0">
                            <div class="col-md-4">
                                <img src="Pictures/indiana.jpg" class="img-fluid rounded-start m-sm-0 m-md-2" alt="indiana">
                            </div>

                            <div class="col-md-8">
                                <div class="card-body">
                                    <h2 class="card-title">Rower wyścigowy Indiana</h2>
                                    <p class="card-text">Tekst o rowerze indiana / stan</p>
                                    <p class="card-text"><b>Cena zakupu: 1200 PLN</b></p>
                                    <p class="card-text"><b>Cena wypożyczenia: 3 PLN /min</b></p>
                                </div>
                            </div>
                        </div>
                    </div>`,

    `<div class="card mb-3">
                        <div class="row g-0">
                            <div class="col-md-4">
                                <img src="Pictures/scooter.jpg" class="img-fluid rounded-start m-sm-0 m-md-2" alt="jivr">
                            </div>

                            <div class="col-md-8">
                                <div class="card-body">
                                    <h2 class="card-title">Hulajnoga elektryczna JIVR</h2>
                                    <p class="card-text">Tekst o hulajnodze / stan</p>
                                    <p class="card-text"><b>Cena zakupu: 1200 PLN</b></p>
                                    <p class="card-text"><b>Cena wypożyczenia: 3 PLN /min</b></p>
                                </div>
                            </div>
                        </div>
                    </div>`
]

function change(id){
    document.getElementById("vehicleInfo").innerHTML = vehicles[id];
}//change