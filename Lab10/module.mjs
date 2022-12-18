/**
 * A class representing a mathematical operation.
 * @class
 */
class Operation {
  /**
   * Creates an instance of Operation.
   * @constructor
   * @param {number} x - The first operand.
   * @param {number} y - The second operand.
   */
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  /**
   * Calculates the sum of the two operands.
   * @returns {number} The sum of the operands.
   */
  sum() {
    return this.x + this.y;
  }
}

/**
 * Exports the Operation class.
 * @module Operation
 */
export { Operation };

/**
 * The default export for the Operation module.
 * @default
 */
export default Operation;

/* CommonJS
module.exports = Operation;
*/
