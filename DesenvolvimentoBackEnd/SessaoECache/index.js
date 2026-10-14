const express = require('express');
app = express();

app.get('/setcookie', (req, res ) => {
    res.cookie('Acesso', `Acesso em ${new Date()}`);
    res.send('Cookie foi salvo com sucesso.');
});

app.listen(3000, () => console.log('Servidor executando..!'));
