const { Console } = require('console');
const os = require('os');

setInterval(()=>{

    const {arch, platform, totalmem, freemem} = os;
    const tRam = parseInt(totalmem() / 1024 / 1024);
    const fRam = parseInt(freemem() / 1024 / 1024);
    const usage = (((fRam / tRam) * 100) - 100) * -1;
    
    const stats = {
        OS: platform(),
        Arch: arch(),
        TotalRAM: `${tRam} MB`,
        FreeRAM: `${fRam} MB`,
        Usage: `${usage.toFixed(2)} %`
    }
    console.clear()
    console.table(stats);
    exports.stats = stats;
}, 1000);