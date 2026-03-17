function maiorElemento(arr: number []): number {
    if (arr.length == 0){
        return -Infinity;
    }

    const ultimoElemento = arr[arr.length - 1];
    const maiorDosRestantes = maiorElemento(arr.slice(0, -1));
    return Math.max(ultimoElemento, maiorDosRestantes);
}

function menorElemento(arr: number []): number {
    if (arr.length == 0){
        return Infinity;
    }
    const ultimoElemento = arr[arr.length - 1];
    const menorDosRestantes = menorElemento(arr.slice(0, -1));
    return Math.min(ultimoElemento, menorDosRestantes);
}


console.log("Menor: " + menorElemento([1, 5, 3, 9, 2]));
console.log("Maior: " + maiorElemento([1, 5, 3, 9, 2]));