let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');

// Napis

ctx.shadowColor = '#825FCA';    // styl cieni
ctx.shadowBlur = 4;
ctx.shadowOffsetX = 2;
ctx.shadowOffsetY = 2;

ctx.strokeRect(25, 10, 142, 65)     // ramka

ctx.lineWidth = 1.5;    // styl napisu
ctx.strokeStyle='#201F1F';

ctx.font = '48px Arial';    // napis
ctx.textAlign = 'center';
ctx.strokeText("Bicykl", 96, 55, 200)

// Rower

ctx.lineWidth = 5;      // styl roweru
ctx.shadowBlur = 14;

ctx.moveTo(53, 112);    // siedzenie
ctx.lineTo(78, 112)

ctx.moveTo(66, 113);    // wsparcie siedzenia
ctx.lineTo(78, 135);

ctx.moveTo(75, 135);    // rama
ctx.lineTo(125, 135);

ctx.moveTo(145, 143);   // wsparcie kierownicy
ctx.lineTo(125, 98);

ctx.moveTo(118, 100);   // kierownica
ctx.lineTo(143, 95);

ctx.moveTo(80, 150);    // lewe koło
ctx.arc(55, 150, 25, 0, 2 * Math.PI, false);

ctx.moveTo(170,150);    // prawe koło
ctx.arc(145, 150, 25, 0, 2 * Math.PI, false);

ctx.stroke();