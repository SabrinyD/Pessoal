import { useState } from "react";

// Definição das interfaces
interface Pessoa {
  id: number;
  nome: string;
  idade: number;
}

interface Transacao {
  id: number;
  descricao: string;
  valor: number;
  tipo: "despesa" | "receita";
  pessoaId: number;
}

const App = () => {
  // Estados para armazenar pessoas e transações
  const [pessoas, setPessoas] = useState<Pessoa[]>([]);
  const [transacoes, setTransacoes] = useState<Transacao[]>([]);

  // Estados para captura de inputs
  const [nome, setNome] = useState("");
  const [idade, setIdade] = useState(0);
  const [descricao, setDescricao] = useState("");
  const [valor, setValor] = useState(0);
  const [tipo, setTipo] = useState<"despesa" | "receita">("despesa");
  const [pessoaId, setPessoaId] = useState<number | null>(null);

  // Função para adicionar uma pessoa
  const adicionarPessoa = () => {
    setPessoas([...pessoas, { id: pessoas.length + 1, nome, idade }]);
    setNome("");
    setIdade(0);
  };

  // Função para adicionar uma transação
  const adicionarTransacao = () => {
    if (pessoaId === null) return;

    const pessoa = pessoas.find(p => p.id === pessoaId);
    if (!pessoa) return;

    // Regra: menores de idade só podem registrar despesas
    if (pessoa.idade < 18 && tipo === "receita") {
      alert("Menores de idade só podem registrar despesas.");
      return;
    }

    setTransacoes([...transacoes, { id: transacoes.length + 1, descricao, valor, tipo, pessoaId }]);
    setDescricao("");
    setValor(0);
  };

  return (
    <div>
      <h2>Cadastro de Pessoas</h2>
      <input placeholder="Nome" value={nome} onChange={(e) => setNome(e.target.value)} />
      <input type="number" placeholder="Idade" value={idade} onChange={(e) => setIdade(Number(e.target.value))} />
      <button onClick={adicionarPessoa}>Adicionar Pessoa</button>

      <h2>Cadastro de Transações</h2>
      <input placeholder="Descrição" value={descricao} onChange={(e) => setDescricao(e.target.value)} />
      <input type="number" placeholder="Valor" value={valor} onChange={(e) => setValor(Number(e.target.value))} />
      <select value={tipo} onChange={(e) => setTipo(e.target.value as "despesa" | "receita")}>
        <option value="despesa">Despesa</option>
        <option value="receita">Receita</option>
      </select>
      <select value={pessoaId ?? ""} onChange={(e) => setPessoaId(Number(e.target.value))}>
        <option value="" disabled>Selecione uma pessoa</option>
        {pessoas.map((p) => (
          <option key={p.id} value={p.id}>{p.nome}</option>
        ))}
      </select>
      <button onClick={adicionarTransacao}>Adicionar Transação</button>
    </div>
  );
};

export default App;