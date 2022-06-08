var roleta = Math.floor(Math.random()*6)
var municaolocal = Math.floor(Math.random()*6)

console.log("Roleta: "+roleta+"\nMunição: "+municaolocal)


if (roleta == municaolocal) {
    console.log("💀🎇🔫")   
}
else{
    console.log("Não foi dessa vez!")
}