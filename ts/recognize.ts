import path from "node:path";
import fs from "node:fs";
import Handlebars from "handlebars";
import { completion } from "litllm";

import { PIICategory } from "./category";

/**
 *
 * @param input a text which may or may not contain PII
 * @param category category of PII to recognize
 * @param customPrompt a custom prompt to use for the recognition (HBS format)
 * @returns the recognized fields in the text
 */
export async function recognize(
  input: string,
  category: PIICategory,
  customPrompt?: string
) {
  let hbs;
  if (customPrompt) {
    hbs = customPrompt;
  } else {
    const filename = path.join(__dirname, `../prompts/${category}.hbs`);
    hbs = fs.readFileSync(filename, "utf-8");
  }

  const template = Handlebars.compile(hbs);

  const message = template({ sentence: input });

  const result = await completion(
    "gpt-4",
    [{ role: "user", content: message }],
    {
      temperature: 0.1,
    }
  );

  const recognitions = JSON.parse(result.message.content);

  const ret: {
    field: string;
    category: string;
    // startIndex: number;
    // endIndex: number;
  }[] = [];

  for (const [key, value] of Object.entries(recognitions)) {
    if (!Array.isArray(value)) {
      continue;
    }

    if (value.length > 0) {
      value.forEach((v) => {
        ret.push({
          field: v,
          category: key,
          // startIndex: input.indexOf(v),
          // endIndex: input.indexOf(v) + v.length,
        });
      });
    }
  }

  return ret;
}
