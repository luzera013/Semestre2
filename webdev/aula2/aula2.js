const URL_PRODUTOS = "https://fakestoreapi.com/products";
let todosOsProdutos = []

const buscarProdutos = async () => {
    const resposta = await fetch(URL_PRODUTOS)
    const dados = await resposta.json()
    todosOsProdutos = dados
    renderizarCard(todosOsProdutos)
    console.log(todosOsProdutos)

}

const renderizarCard = ListaProdutos => {
    const grid = document.querySelector("#grid-categoria")
    grid.innerHTML = ""

    listaProdutos.forEach(produto => {
        const card = document.createElement("article");
        card.className = "card";
        card.innerHTML = `
        <img src="${produto.image}" alt="${produto.title}" />
        <h3>${produto.title}</h3>
        <p class="preco">R$ ${produto.price.toFixed(2)}</p>
        <p class="avaliacao">⭐ ${produto.rating.rate} (${produto.rating.count} avaliações)</p>`

        grid.append(card)
    })
}





buscarProdutos();