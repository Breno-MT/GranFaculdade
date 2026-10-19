import { open, close, appendFile } from "node:fs";
import { fileURLToPath } from 'url';
import path from "path";
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.resolve(__dirname, "..", "log.txt");

const closeArq = (fd) => {
  close(fd, (err) => {
    if (err) throw err;
  });
};

open(filePath, "a", (err, fd) => {
  if (err) throw err;
  appendFile(fd, `Escrito Y em ${new Date()}\n`, "utf8", (err) => {
    closeArq(fd);
    if (err) throw err;
  });
});
