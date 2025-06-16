import { Parsed, Row } from "./types";
/**
 * An tabular object with rows and columns and cells values of either
 * number, string, or boolean
 */
export interface DataSet {
    /** The number of cases */
    n: number;
    /** keys of columns */
    keys: Array<string>;
    /** The names of the columns */
    names: Map<string, string>;
    /** The map of unique column names to descriptive labels */
    labels: Map<string, string>;
    /**
     * Get a single row of data as a {@link Map} dictionary of key-values
     * @param index the row index
     * @returns a {@link Row}
     */
    row(index: number): Row;
    /**
     * Get a single column of data as an Array
     * @param key the key of the column
     * @returns an Array of either numbers, strings or booleans
     */
    col(key: string): Array<number> | Array<string> | Array<boolean>;
    /**
     *
     * @param index row index
     * @param keys column key
     * @returns a string number or boolean at the cell address
     */
    cell(index: number, key: string): string | number | boolean;
    /**
     * Subset the object by row and/or column identifiers
     * @param indices an optional Array of row indices
     * @param keys an optional Array of column names
     * @returns a subset {@link DataSet}
     */
    view(indices?: Array<number>, keys?: Array<string>): DataSet;
}
declare abstract class Column<U extends number | string | boolean, T extends U | string = U> {
    protected parent: Savvy;
    protected key: string;
    protected nulls: Set<U>;
    constructor(parent: Savvy, key: string, nulls: Set<U>);
    abstract cast(value: U): T;
    abstract measure: 'nominal' | 'ordinal' | 'scale' | 'null';
    abstract levels: Map<U, T>;
    raw(): Array<U>;
    get values(): Array<T>;
    exists(): boolean;
    get name(): string;
    get label(): string;
    get missing(): Set<U>;
    set missing(nulls: Set<U>);
    ismissing(value: U): boolean;
}
/**
 * A DataSet subclass that can be constructed from a {@link Parsed} object
 */
export declare class Savvy implements DataSet {
    private cases;
    private data;
    private overflows;
    private fields;
    private _names;
    private _labels;
    /**
     *
     * @param parsed a {@link Parsed} object generated with a {@link SavParser}
     */
    constructor(parsed: Parsed);
    get n(): number;
    get keys(): Array<string>;
    /**
     * A map of of unique column keys to variable names
     */
    get names(): Map<string, string>;
    set names(names: Map<string, string>);
    /**
     * A map of of unique column keys to longer labels
     */
    get labels(): Map<string, string>;
    set labels(labels: Map<string, string>);
    row(index: number, cast?: boolean): Row;
    field(key: string): Column<string | number | boolean>;
    col(key: string, cast?: boolean): Array<number> | Array<string> | Array<boolean>;
    cell(index: number, key: string, cast?: boolean): number | string | boolean;
    view(indices?: Array<number>, fields?: Array<string>): DataSet;
}
export {};
