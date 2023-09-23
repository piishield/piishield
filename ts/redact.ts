import { PIICategory } from "./category";
import { recognize } from "./recognize";

/**
 *
 * @param input a text which may or may not contain PII
 * @param category category of PII to recognize
 * @returns the text with the PII category redacted
 */
export async function redact(input: string, category: PIICategory) {
  const recognitions = await recognize(input, category);

  let output = input;
  for (const recognition of recognitions) {
    output = output.replace(recognition.field, `[${category.toUpperCase()}]`);
  }

  return output;
}
