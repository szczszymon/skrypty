import Operation from './module.mjs';

/* CommonJS
const Operation = require('./module');
*/
const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);
const operation = new Operation(x, y);
console.log(operation.sum()); // wyświetli 3
