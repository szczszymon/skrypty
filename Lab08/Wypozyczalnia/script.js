let borrowed = [];
let borrowers = [];
let vehicles = [
    ["Rower", "Hiland", "https://m.media-amazon.com/images/I/51g9q7GIhqL.jpg"],
    ["Rower", "Indiana", "https://www.electro.pl/media/cache/gallery/product/3/165/854/443/iyxu5j7c/images/35/3574837/INDIANA-X-Pulser-2-7-M17-27-5-cala-meski-Czarno-zolty-skos.jpg"],
    ["Hulajnoga", "JIVR", "https://www.skatehut.co.uk/media/catalog/product/cache/cc9d12ca4c12746d69496c308c0d4e29/J/I/JIV_222_ELE_SCO_PLU_00_7b36.jpg"]
];
let state = [
    [vehicles[0], 0],
    [vehicles[1], 0],
    [vehicles[2], 0]
];
let total = [
    [vehicles[0], 0],
    [vehicles[1], 0],
    [vehicles[2], 0]
];

function detect(){
    let command = document.getElementById("input").value;
    command = command.split(' ');

    if (command.length <= 0) {
        alert("Błąd składni: ");
        return;
    }// if

    switch (command[0]){
        case "set":
        case "ustaw":
            set(command.slice(1));
            break;

        case "borrow":
        case "wypożycz":
        case "wypozycz":
            borrow(command.slice(1));
            break;

        case "return":
        case "zwróć":
        case "zwroc":
            ret(command.slice(1));
            break;

        case "list":
        case "wypisz":
            list();
            break;

        case "available":
        case "dostępne":
        case "dostepne":
            available();
            break;

        case "help":
        case "operacje":
            alert("Dozwolone operacje: ustaw, wypożycz, zwróć, wypisz, dostępne, operacje");
            return;

        default:
            alert("Błąd składni: operacja niedozwolona");
            return;
    }//switch
    myChart.data.datasets[0].data = [state[0][1], state[1][1], state[2][1]];
    myChart.data.datasets[1].data = [total[0][1], total[1][1], total[2][1]];
    myChart.update();
}// detect()

function set(args){
    if (args.length <= 0) {
        empty()
        return;
    }// if
    else if (args.length < 3){
        alert("Błąd składni: min liczba argumentów operacji: 3 (set [rodzaj] [marka] [ilość], ...)")
        return;
    }// else if

    args = args.join(' ');
    args = args.split(",");

    for (let i = 0; i < args.length; i++) {
        args[i] = args[i].trim();
    }// for

    for (let i = 0; i < 3; i++) {
        let data = args[i].split(" ");

        if (isNaN(parseInt(data[2]))){
            badInt();
            return;
        }// if

        switch (data[0]){
            case "rower":
            case "Rower":
                switch (data[1]){
                    case "hiland":
                    case "Hiland":
                        state[0][1] = parseInt(data[2]);
                        total[0][1] = parseInt(data[2]);
                        break;

                    case "indiana":
                    case "Indiana":
                        state[1][1] = parseInt(data[2]);
                        total[1][1] = parseInt(data[2]);
                        break;

                    default:
                        alert("Błąd składni: podano złą markę");
                        return;
                }//switch
                break;

            case "hulajnoga":
            case "Hulajnoga":
                switch (data[1]) {
                    case "jivr":
                    case "JIVR":
                        state[2][1] = parseInt(data[2]);
                        total[2][1] = parseInt(data[2]);
                        break;

                    default:
                        alert("Błąd składni: podano złą markę");
                        return;
                }//switch
                break;

            default:
                alert("Błąd składni: podano zły rodzaj pojazdu");
                return;
        }// switch
    }// for
}// set()

function borrow(args){
    if (args.length <= 0) {
        empty()
        return;
    }// if
    else if (args.length < 3 || args.length > 6){
        alert("Błąd składni: min liczba argumentów operacji: 6 (borrow [rodzaj] [marka] [ilość] [czas] [imie] [nazwisko])")
        return;
    }// else if

    if (isNaN(parseInt(args[2]))){
        badInt();
        return;
    }// if

    if (!borrowersContain(args[4], args[5]))
        borrowers.push([args[4], args[5]]);

    let index = findID(args[4], args[5]);

    switch (args[0]){
        case "rower":
        case "Rower":
            switch (args[1]){
                case "hiland":
                case "Hiland":
                    if (state[0][1] - parseInt(args[2]) < 0){
                        notInStock(1);
                        return;
                    }// if
                    else if (state[0][1] === 0){
                        notInStock(0);
                        return;
                    }//else if

                    state[0][1] -= parseInt(args[2]);
                    if (borrowedContain(vehicles[0], borrowers[index], parseInt(args[3]))){
                        let borrowIndex = borrowedFindID(vehicles[0], borrowers[index], parseInt(args[3]));
                        borrowed[borrowIndex][2] += parseInt(args[2]);
                    }// if
                    else
                        borrowed.push([vehicles[0], borrowers[index], parseInt(args[2]), parseInt(args[3])]);
                    break;

                case "indiana":
                case "Indiana":
                    if (state[1][1] - parseInt(args[2]) < 0){
                        notInStock(1);
                        return;
                    }// if
                    else if (state[1][1] === 0){
                        notInStock(0);
                        return;
                    }//else if

                    state[1][1] -= parseInt(args[2]);
                    if (borrowedContain(vehicles[1], borrowers[index], parseInt(args[3]))){
                        let borrowIndex = borrowedFindID(vehicles[1], borrowers[index], parseInt(args[3]));
                        borrowed[borrowIndex][2] += parseInt(args[2]);
                    }// if
                    else
                        borrowed.push([vehicles[1], borrowers[index], parseInt(args[2]), parseInt(args[3])]);
                    break;

                default:
                    alert("Błąd składni: podano złą markę");
                    return;
            }//switch
            break;

        case "hulajnoga":
        case "Hulajnoga":
            switch (args[1]) {
                case "jivr":
                case "JIVR":
                    if (state[2][1] - parseInt(args[2]) < 0){
                        notInStock(1);
                        return;
                    }// if
                    else if (state[2][1] === 0){
                        notInStock(0);
                        return;
                    }//else if

                    state[2][1] -= parseInt(args[2]);
                    if (borrowedContain(vehicles[2], borrowers[index], parseInt(args[3]))){
                        let borrowIndex = borrowedFindID(vehicles[2], borrowers[index], parseInt(args[3]));
                        borrowed[borrowIndex][2] += parseInt(args[2]);
                    }// if
                    else
                        borrowed.push([vehicles[2], borrowers[index], parseInt(args[2]), parseInt(args[3])]);
                    break;

                default:
                    alert("Błąd składni: podano złą markę");
                    return;
            }//switch
            break;

        default:
            alert("Błąd składni: podano zły rodzaj pojazdu");
            return;
    }// switch

}// borrow()

function ret(args){
    if (args.length <= 0) {
        empty();
        return;
    }// if
    else if (args.length < 3 || args.length > 6){
        alert("Błąd składni: min liczba argumentów operacji: 6 (return [rodzaj] [marka] [ilość] [czas] [imie] [nazwisko])");
        return;
    }// else if

    if (!borrowersContain(args[4], args[5])) {
        alert("Błąd zwrotu: dana osoba nigdy nie dokonała wypożyczenia");
        return;
    }//if

    let index = findID(args[4], args[5]);

    switch (args[0]){
        case "rower":
        case "Rower":
            switch (args[1]){
                case "hiland":
                case "Hiland":
                    if (!borrowedContain(vehicles[0], borrowers[index], parseInt(args[3]))){
                        alert("Błąd zwrotu: dana osoba nigdy nie wypożyczyła takiego pojazdu");
                        return;
                    }// if
                    else {
                        let borrowIndex = borrowedFindID(vehicles[0], borrowers[index], parseInt(args[3]));

                        if (borrowed[borrowIndex][2] < parseInt(args[2])) {
                            alert("Błąd zwrotu: dana osoba chce zwrócić więcej sztuk pojazdu niż wypożyczyła")
                            return;
                        }// if

                        state[0][1] += parseInt(args[2]);

                        if (borrowed[borrowIndex][2] === parseInt(args[2]))
                            borrowed.splice(borrowIndex, 1);
                        else
                            borrowed[borrowIndex][2] -= parseInt(args[2]);

                        if (!borrowedContainPerson(borrowers[index]))
                            borrowers.splice(index, 1);
                    }// else
                    break;

                case "indiana":
                case "Indiana":
                    if (!borrowedContain(vehicles[1], borrowers[index], parseInt(args[3]))){
                        alert("Błąd zwrotu: dana osoba nigdy nie wypożyczyła takiego pojazdu");
                        return;
                    }// if
                    else {
                        let borrowIndex = borrowedFindID(vehicles[1], borrowers[index], parseInt(args[3]));

                        if (borrowed[borrowIndex][2] < parseInt(args[2])) {
                            alert("Błąd zwrotu: dana osoba chce zwrócić więcej sztuk pojazdu niż wypożyczyła")
                            return;
                        }// if

                        state[1][1] += parseInt(args[2]);

                        if (borrowed[borrowIndex][2] === parseInt(args[2]))
                            borrowed.splice(borrowIndex, 1);
                        else
                            borrowed[borrowIndex][2] -= parseInt(args[2]);

                        if (!borrowedContainPerson(borrowers[index]))
                            borrowers.splice(index, 1);
                    }// else
                    break;

                default:
                    alert("Błąd składni: podano złą markę");
                    return;
            }//switch
            break;

        case "hulajnoga":
        case "Hulajnoga":
            switch (args[1]) {
                case "jivr":
                case "JIVR":
                    if (!borrowedContain(vehicles[2], borrowers[index], parseInt(args[3]))){
                        alert("Błąd zwrotu: dana osoba nigdy nie wypożyczyła takiego pojazdu");
                        return;
                    }// if
                    else {
                        let borrowIndex = borrowedFindID(vehicles[2], borrowers[index], parseInt(args[3]));

                        if (borrowed[borrowIndex][2] < parseInt(args[2])) {
                            alert("Błąd zwrotu: dana osoba chce zwrócić więcej sztuk pojazdu niż wypożyczyła")
                            return;
                        }// if

                        state[2][1] += parseInt(args[2]);

                        if (borrowed[borrowIndex][2] === parseInt(args[2]))
                            borrowed.splice(borrowIndex, 1);
                        else
                            borrowed[borrowIndex][2] -= parseInt(args[2]);

                        if (!borrowedContainPerson(borrowers[index]))
                            borrowers.splice(index, 1);
                    }// else
                    break;

                default:
                    alert("Błąd składni: podano złą markę");
                    return;
            }//switch
            break;

        default:
            alert("Błąd składni: podano zły rodzaj pojazdu");
            return;
    }// switch
}// ret()

function list(){
    for (let person of borrowers){
        let output = "";
        let kwota = 0;
        output += person[0] + " " + person[1] + ": ";

        for (let item of borrowed){
            if (person[0] === item[1][0] && person[1] === item[1][1]){
                kwota += 3 * parseInt(item[3]) * parseInt(item[2]);
                output += item[0][0] + " " + item[0][1] + " w ilości:" + item[2] + " na czas:" + item[3] + " minut o wartości:" + parseInt(item[3]) * 3 * parseInt(item[2]) + "zł\n";
            }//if
        }// for
        output += "Łączna wartość wypożyczeń: " + kwota;
        console.log(output);
    }// for
}// list()

function available(){
    let output = "";

    for (let i = 0; i < 3; i++){
        output += state[i][0][0] + " " + state[i][0][1] + " Ilość dostępnych sztuk: " + state[i][1] + "\n";
    }// for

    console.log(output);
}// available()

function borrowersContain(name, surname){
    return borrowers.some((element) => element[0] === name && element[1] === surname);
}// borrowersContain()

function borrowedContain(vehicle, person, time){
    for (let i = 0; i < borrowed.length; i++) {
        if (borrowed[i][0][0] === vehicle[0] && borrowed[i][0][1] === vehicle[1] && borrowed[i][1][0] === person[0] && borrowed[i][1][1] === person[1] && borrowed[i][3] === time)
            return true;
    }// for
    return false;
}// borrowedContain()

function borrowedContainPerson(person){
    for (let i = 0; i < borrowed.length; i++) {
        if (borrowed[i][1][0] === person[0] && borrowed[i][1][1] === person[1])
            return true;
    }// for
    return false;
}// borrowedContain()
function borrowedFindID(vehicle, person, time){
    for (let i = 0; i < borrowed.length; i++) {
        if (borrowed[i][0][0] === vehicle[0] && borrowed[i][0][1] === vehicle[1] && borrowed[i][1][0] === person[0] && borrowed[i][1][1] === person[1] && borrowed[i][3] === time)
            return i;
    }// for
}// borrowedFindID()

function findID(name, surname){
    const check = (element) => element[0] === name && element[1] === surname;
    return borrowers.findIndex(check);
}// findID()

function empty(){
    alert("Błąd składni: brak argumentów dla właściwej operacji");
}// empty()

function badInt(){
    alert("Błąd argumentu: argument ilości nie jest liczbą");
}// badInt()

function notInStock(err){
    switch (err){
        case 0:
            alert("Błąd wypożyczenia: pojazd nie jest dostępny");
            break;

        case 1:
            alert("Błąd wypożyczenia: pojazd dostępny w ograniczonej ilości")
            break;
    }// switch
}// notInStock()