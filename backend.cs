using System;
using System.Collections.Generic;
using System.Linq;

// Classe que representa uma pessoa cadastrada no sistema
public class Pessoa
{
    public int Id { get; set; } // Identificador único
    public string Nome { get; set; } // Nome da pessoa
    public int Idade { get; set; } // Idade da pessoa
}

// Classe que representa uma transação financeira
public class Transacao
{
    public int Id { get; set; } // Identificador único da transação
    public string Descricao { get; set; } // Descrição da transação
    public decimal Valor { get; set; } // Valor positivo da transação
    public string Tipo { get; set; } // "despesa" ou "receita"
    public int PessoaId { get; set; } // ID da pessoa associada
}

public class SistemaGastos
{
    private List<Pessoa> pessoas = new List<Pessoa>(); // Lista de pessoas
    private List<Transacao> transacoes = new List<Transacao>(); // Lista de transações
    private int pessoaIdCounter = 1;
    private int transacaoIdCounter = 1;

    // Cadastra uma nova pessoa
    public void CadastrarPessoa(string nome, int idade)
    {
        pessoas.Add(new Pessoa { Id = pessoaIdCounter++, Nome = nome, Idade = idade });
    }

    // Exclui uma pessoa e suas transações associadas
    public void ExcluirPessoa(int pessoaId)
    {
        pessoas.RemoveAll(p => p.Id == pessoaId);
        transacoes.RemoveAll(t => t.PessoaId == pessoaId);
    }

    // Cadastra uma transação para uma pessoa
    public void CadastrarTransacao(string descricao, decimal valor, string tipo, int pessoaId)
    {
        var pessoa = pessoas.FirstOrDefault(p => p.Id == pessoaId);
        if (pessoa == null) throw new Exception("Pessoa não encontrada.");

        // Restrição para menores de idade
        if (pessoa.Idade < 18 && tipo.ToLower() == "receita")
            throw new Exception("Menores de idade só podem registrar despesas.");

        transacoes.Add(new Transacao { Id = transacaoIdCounter++, Descricao = descricao, Valor = valor, Tipo = tipo, PessoaId = pessoaId });
    }

    // Lista todas as pessoas cadastradas com seus totais
    public void ConsultarTotais()
    {
        decimal totalReceitas = 0, totalDespesas = 0;

        foreach (var pessoa in pessoas)
        {
            var receitas = transacoes.Where(t => t.PessoaId == pessoa.Id && t.Tipo == "receita").Sum(t => t.Valor);
            var despesas = transacoes.Where(t => t.PessoaId == pessoa.Id && t.Tipo == "despesa").Sum(t => t.Valor);

            Console.WriteLine($"{pessoa.Nome}: Receita = {receitas:C}, Despesa = {despesas:C}, Saldo = {(receitas - despesas):C}");

            totalReceitas += receitas;
            totalDespesas += despesas;
        }

        Console.WriteLine($"Total Geral: Receita = {totalReceitas:C}, Despesa = {totalDespesas:C}, Saldo = {(totalReceitas - totalDespesas):C}");
    }
}