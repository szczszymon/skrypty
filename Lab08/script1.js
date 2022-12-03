function wypisz(){
    let tekst = document.forms[0].elements[0].value
    let liczba = document.forms[0].elements[1].value
    alert('Pole Tekstowe: ' + tekst + '\nPole Liczbowe: ' + liczba);
    alert('Typ pola tekstowego: ' + typeof tekst + '\nTyp pola liczbowego: ' + typeof liczba)
}


let dane = window.prompt('Tekst1', "Tekst2");
console.log(dane, typeof dane)