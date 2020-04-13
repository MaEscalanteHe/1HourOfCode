const mysql = require('promise-mysql');

const connection = mysql.createConnection({
	host: 'localhost',
	user: 'mysql',
	password: 'mysql_password_testing666',
	database: 'electrondb',
});

function getConnection() {
	return connection;
}

module.exports = { getConnection };
