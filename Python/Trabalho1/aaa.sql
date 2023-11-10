WITH CTE_Vendas AS (
    SELECT
        Cliente.ID AS ClienteID,
        Produto.Categoria AS CategoriaProduto,
        AVG(Pedido.ValorTotal) AS MediaValorTotal,
        RANK() OVER(PARTITION BY Produto.Categoria ORDER BY AVG(Pedido.ValorTotal) DESC) AS ClassificacaoCategoria
    FROM
        Cliente
    INNER JOIN
        Pedido ON Cliente.ID = Pedido.IDCliente
    INNER JOIN
        ItemPedido ON Pedido.ID = ItemPedido.IDPedido
    INNER JOIN
        Produto ON ItemPedido.IDProduto = Produto.ID
    WHERE
        Cliente.Ativo = 1
    GROUP BY
        Cliente.ID, Produto.Categoria
    HAVING
        COUNT(Pedido.ID) > 10
),
CTE_TopCategorias AS (
    SELECT
        CategoriaProduto,
        AVG(MediaValorTotal) AS MediaGeralCategoria
    FROM
        CTE_Vendas
    GROUP BY
        CategoriaProduto
),
CTE_TopClientes AS (
    SELECT
        ClienteID,
        CategoriaProduto,
        MediaValorTotal,
        ClassificacaoCategoria
    FROM
        CTE_Vendas
    WHERE
        ClassificacaoCategoria <= 3
)
SELECT
    Cliente.Nome AS NomeCliente,
    CTE_TopClientes.CategoriaProduto,
    CTE_TopClientes.MediaValorTotal,
    CTE_TopCategorias.MediaGeralCategoria
FROM
    Cliente
LEFT JOIN
    CTE_TopClientes ON Cliente.ID = CTE_TopClientes.ClienteID
LEFT JOIN
    CTE_TopCategorias ON CTE_TopClientes.CategoriaProduto = CTE_TopCategorias.CategoriaProduto
WHERE
    CTE_TopClientes.ClassificacaoCategoria IS NOT NULL
ORDER BY
    CTE_TopClientes.CategoriaProduto, CTE_TopClientes.ClassificacaoCategoria;
