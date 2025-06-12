// confuser.js
const fs = require("fs");
const JsConfuser = require("js-confuser");

(async () => {
  const inputFile = process.argv[2];
  const outputFile = process.argv[3];

  const code = fs.readFileSync(inputFile, "utf-8");

  const obfuscatedCode = await JsConfuser.obfuscate(code, {
    target: "node",
    calculator: false,
    compact: true,
    controlFlowFlattening: 1,
    deadCode: 1,
    dispatcher: true,
    duplicateLiteralsRemoval: 1,
    es5: true,
    flatten: true,
    globalConcealing: true,
    hexadecimalNumbers: false,
    identifierGenerator: function () {
      const unicodeCharsStart = ['break', '火火火', 'if'];
      const unicodeCharsEnd = ['const', '气‌和气‌', 'return'];
      const randomString = Math.random().toString(36).substring(2, 12);
      const charStart = unicodeCharsStart[Math.floor(Math.random() * unicodeCharsStart.length)];
      const charEnd = unicodeCharsEnd[Math.floor(Math.random() * unicodeCharsEnd.length)];
      return `$${charStart}‌$${randomString}$${charEnd}$`;
    },
    lock: {
      antiDebug: 1,
      integrity: 1,
      selfDefending: true,
    },
    minify: true,
    movedDeclarations: true,
    objectExtraction: true,
    opaquePredicates: true,
    renameGlobals: true,
    renameVariables: true,
    shuffle: {
      hash: 1,
      true: 1,
    },
    stack: true,
    stringCompression: true,
    stringConcealing: true,
    stringEncoding: 0.05,
    stringSplitting: true,
  });

  const header = `
/*
~ Kode di-obfuscate Hard Obf
~ Telegram: t.me/BirdCella
~ Covz Confuser Unicode Type

© Cella

🔐 Owner : Cella

📘 Obf Version : 3.1

🔩 Type : JS

📆 Date : ${new Date().toISOString().split('T')[0]}

⚔️ Support : NodeJS, Termux

❄ Node Module : 3
*/
`;

  const finalCode = `${header}\n${obfuscatedCode}`;

  fs.writeFileSync(outputFile, finalCode, "utf-8");
})();
