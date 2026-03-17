function somaArray(arr: number[], elementos: number): number{
    if (elementos == 0){
        return 1;
    }
    return arr[elementos - 1] + somaArray(arr, elementos - 1);
}

console.log(somaArray([1, 2, 3, 4], 4));