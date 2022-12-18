const fs = require('fs');

const path = process.argv[2];

try {
  const stats = fs.statSync(path);
  if (stats.isFile()) {
    console.log(`${path} jest plikiem`);
    console.log(fs.readFileSync(path, 'utf-8'));
  } else if (stats.isDirectory()) {
    console.log(`${path} jest katalogiem`);
  } else {
    console.log(`${path} to ani plik, ani katalog`);
  }
} catch (error) {
  console.error(`Nie udało się odczytać informacji o pliku ${path}: ${error}`);
}
