const express = require('express');
const app = express();
const PORT = 3000;

app.get('/check', (req, res) => {
  res.status(200).send('OK');
});

app.get('/info', (req, res) => {
  res.status(200).json({
        "Instancia": "Maquina 2 - Api 2",
        "Curso": "Seminario de Sistemas 1 A",
        "Grupo": "Grupo 4"});
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
