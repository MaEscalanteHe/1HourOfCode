const productForm = document.getElementById('productForm');

const { remote } = require('electron');
const main = remote.require('./main');

const productName = document.getElementById('name');
const productPrice = document.getElementById('price');
const productDescription = document.getElementById('description');
const productsList = document.getElementById('products');

let products = [];
let editingStatus = false;
let editProductID = '';

productForm.addEventListener('submit', async (e) => {
	e.preventDefault();

	const newProduct = {
		name: productName.value,
		price: productPrice.value,
		description: productDescription.value,
	};

	if (!editingStatus) {
		const result = await main.createProduct(newProduct);
		console.log(result);
	} else {
		await main.updateProduct(editProductID, newProduct);
		editingStatus = false;
		editProductID = '';
	}

	productForm.reset();
	productName.focus();

	getProduct();
});

async function deleteProduct(id) {
	const response = await confirm('Are your sure you want to delete it?');
	if (response) {
		await main.deleteProduct(id);
		getProduct();
	}
	return;
}

async function editProduct(id) {
	const product = await main.getProductById(id);
	productName.value = product.name;
	productPrice.value = product.price;
	productDescription.value = product.description;

	editingStatus = true;
	editProductID = product.id;
}

function renderProducts(products) {
	productsList.innerHTML = '';
	products.forEach((product) => {
		productsList.innerHTML += `
		<div class="card card-body my-2 animated fadeInLeft">
			<h4>${product.name}</h4>
			<p>${product.description}</p>
			<h3>${product.price}</h3>
			<p>
				<button class="btn btn-danger" onclick="deleteProduct('${product.id}')">
					DELETE
				</button>
				<button class="btn btn-secondary" onclick="editProduct('${product.id}')">
					EDIT
				</button>
		</div>
		`;
	});
}

const getProduct = async () => {
	products = await main.getProducts();
	renderProducts(products);
};

async function init() {
	await getProduct();
}

init();
