import { program } from "commander";
import { recognize } from "./recognize";
import { redact } from "./redact";

program
  .command("recognize")
  .description("recognize PII in a sentence")
  .argument("<sentence>", "input sentence to recognize")
  .requiredOption("--category <category>", "category of recognition")
  .action(async (input, options) => {
    console.log(await recognize(input, options.category));
  });

program
  .command("redact")
  .description("redact PII in a sentence")
  .argument("<sentence>", "input sentence to redact")
  .requiredOption("--category <category>", "category of redaction")
  .action(async (input, options) => {
    console.log(await redact(input, options.category));
  });

program.parse(process.argv);
