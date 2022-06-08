convertorNumber = 55
convertorType = "F"

if (convertorType == "C") {
    convertido = (convertorNumber-32) * (5/9)
    console.log(""+convertorNumber+"°F são exatamente "+Math.floor(convertido)+"° celsius.")
}

else if (convertorType == "F") {
    convertido = (9*convertorNumber+160) / 5
    console.log(""+convertorNumber+"°C são exatamente "+Math.floor(convertido)+"°F.")
}