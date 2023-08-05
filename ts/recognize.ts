import { PIICategory } from "./category";

/**
 * 
 * @param input a text which may or may not contain PII
 * @param category category of PII to recognize
 * @returns the recognized fields in the text
 */
function recognize(input: string, category: PIICategory) {
  return [{startIndex: -1, endIndex: -1, field: ""}]
}