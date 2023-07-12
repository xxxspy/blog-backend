console.log('loaded...savvy');
(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory();
	else if(typeof define === 'function' && define.amd)
		define("savvy", [], factory);
	else if(typeof exports === 'object')
		exports["savvy"] = factory();
	else
		root["savvy"] = factory();
})(self, () => {
return /******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ([
/* 0 */,
/* 1 */
/***/ ((__unused_webpack_module, exports) => {



function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread(); }
function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _iterableToArray(iter) { if (typeof Symbol !== "undefined" && iter[Symbol.iterator] != null || iter["@@iterator"] != null) return Array.from(iter); }
function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) return _arrayLikeToArray(arr); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) arr2[i] = arr[i]; return arr2; }
function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }
function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }
function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }
function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }
function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }
function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }
function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(arg) { var key = _toPrimitive(arg, "string"); return _typeof(key) === "symbol" ? key : String(key); }
function _toPrimitive(input, hint) { if (_typeof(input) !== "object" || input === null) return input; var prim = input[Symbol.toPrimitive]; if (prim !== undefined) { var res = prim.call(input, hint || "default"); if (_typeof(res) !== "object") return res; throw new TypeError("@@toPrimitive must return a primitive value."); } return (hint === "string" ? String : Number)(input); }
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Savvy = void 0;
var Column = /*#__PURE__*/function () {
  function Column(parent, key, nulls) {
    _classCallCheck(this, Column);
    this.parent = parent;
    this.key = key;
    this.nulls = nulls;
  }
  _createClass(Column, [{
    key: "raw",
    value: function raw() {
      var _this = this;
      return new Array(this.parent.n).fill(0).map(function (_, idx) {
        return _this.parent.cell(idx, _this.key, false);
      });
    }
  }, {
    key: "values",
    get: function get() {
      var _this2 = this;
      return this.raw().map(function (value) {
        return _this2.cast(value);
      });
    }
  }, {
    key: "exists",
    value: function exists() {
      return true;
    }
  }, {
    key: "name",
    get: function get() {
      var _a;
      return (_a = this.parent.names.get(this.key)) !== null && _a !== void 0 ? _a : this.key;
    }
  }, {
    key: "label",
    get: function get() {
      var _a;
      return (_a = this.parent.labels.get(this.key)) !== null && _a !== void 0 ? _a : '';
    }
  }, {
    key: "missing",
    get: function get() {
      return new Set(this.nulls);
    },
    set: function set(nulls) {
      this.nulls = new Set(nulls);
    }
  }, {
    key: "ismissing",
    value: function ismissing(value) {
      return this.nulls.has(value);
    }
  }]);
  return Column;
}();
var NullColumn = /*#__PURE__*/function (_Column) {
  _inherits(NullColumn, _Column);
  var _super = _createSuper(NullColumn);
  function NullColumn(parent) {
    _classCallCheck(this, NullColumn);
    return _super.call(this, parent, '<NULL>', new Set());
  }
  _createClass(NullColumn, [{
    key: "exists",
    value: function exists() {
      return false;
    }
  }, {
    key: "raw",
    value: function raw() {
      return new Array(this.parent.n).fill(null);
    }
  }, {
    key: "values",
    get: function get() {
      return new Array(this.parent.n).fill(null);
    }
  }, {
    key: "cast",
    value: function cast(value) {
      return null;
    }
  }, {
    key: "measure",
    get: function get() {
      return 'null';
    }
  }, {
    key: "levels",
    get: function get() {
      return new Map();
    }
  }]);
  return NullColumn;
}(Column);
var StrColumn = /*#__PURE__*/function (_Column2) {
  _inherits(StrColumn, _Column2);
  var _super2 = _createSuper(StrColumn);
  function StrColumn() {
    _classCallCheck(this, StrColumn);
    return _super2.apply(this, arguments);
  }
  _createClass(StrColumn, [{
    key: "cast",
    value: function cast(value) {
      return this.ismissing(value) ? null : value;
    }
  }, {
    key: "measure",
    get: function get() {
      return 'nominal';
    }
  }, {
    key: "levels",
    get: function get() {
      return new Map();
    }
  }]);
  return StrColumn;
}(Column);
var FacColumn = /*#__PURE__*/function (_Column3) {
  _inherits(FacColumn, _Column3);
  var _super3 = _createSuper(FacColumn);
  function FacColumn(parent, key, levels, nulls, type) {
    var _this3;
    _classCallCheck(this, FacColumn);
    _this3 = _super3.call(this, parent, key, nulls);
    _this3._levels = levels;
    _this3.type = type;
    return _this3;
  }
  _createClass(FacColumn, [{
    key: "cast",
    value: function cast(value) {
      return this.ismissing(value) ? null : this._levels.get(value);
    }
  }, {
    key: "measure",
    get: function get() {
      switch (this.type) {
        case 3:
          return 'scale';
        case 2:
          return 'ordinal';
        default:
          return 'nominal';
      }
    }
  }, {
    key: "levels",
    get: function get() {
      return new Map(_toConsumableArray(this._levels));
    },
    set: function set(levels) {
      var _this4 = this;
      levels.forEach(function (value, key) {
        if (_this4._levels.has(key)) {
          _this4._levels.set(key, value);
        }
      });
    }
  }]);
  return FacColumn;
}(Column);
var NumColumn = /*#__PURE__*/function (_Column4) {
  _inherits(NumColumn, _Column4);
  var _super4 = _createSuper(NumColumn);
  function NumColumn(parent, key, nulls, nullrange, type) {
    var _this5;
    _classCallCheck(this, NumColumn);
    _this5 = _super4.call(this, parent, key, nulls);
    _this5.nullrange = nullrange;
    _this5.type = type;
    return _this5;
  }
  _createClass(NumColumn, [{
    key: "cast",
    value: function cast(value) {
      return this.ismissing(value) ? null : value;
    }
  }, {
    key: "measure",
    get: function get() {
      switch (this.type) {
        case 2:
          return 'ordinal';
        default:
          return 'scale';
      }
    }
  }, {
    key: "levels",
    get: function get() {
      return new Map();
    }
  }, {
    key: "ismissing",
    value: function ismissing(value) {
      return this.nulls.has(value) || value > this.nullrange[0] && value < this.nullrange[1];
    }
  }]);
  return NumColumn;
}(Column);
var View = /*#__PURE__*/function () {
  function View(parent, indices, keys) {
    _classCallCheck(this, View);
    var _a, _b;
    this.parent = parent;
    this.indices = (_a = indices === null || indices === void 0 ? void 0 : indices.slice()) !== null && _a !== void 0 ? _a : new Array(parent.n).fill(0).map(function (_, idx) {
      return idx;
    });
    this._keys = (_b = keys === null || keys === void 0 ? void 0 : keys.slice()) !== null && _b !== void 0 ? _b : Array.from(parent.names.keys());
  }
  _createClass(View, [{
    key: "n",
    get: function get() {
      return this.indices.length;
    }
  }, {
    key: "keys",
    get: function get() {
      return _toConsumableArray(this._keys);
    }
  }, {
    key: "names",
    get: function get() {
      var names = this.parent.names;
      return new Map(this.keys.map(function (key) {
        var _a;
        return [key, (_a = names.get(key)) !== null && _a !== void 0 ? _a : key];
      }));
    }
  }, {
    key: "labels",
    get: function get() {
      var labels = this.parent.labels;
      return new Map(this.keys.map(function (key) {
        var _a;
        return [key, (_a = labels.get(key)) !== null && _a !== void 0 ? _a : ''];
      }));
    }
  }, {
    key: "row",
    value: function row(index) {
      return this.parent.row(this.indices[index]);
    }
  }, {
    key: "col",
    value: function col(key) {
      var all = this.parent.col(key);
      return this.indices.map(function (index) {
        return all[index];
      });
    }
  }, {
    key: "cell",
    value: function cell(index, key) {
      return this.parent.cell(this.indices[index], key);
    }
  }, {
    key: "view",
    value: function view(indices, keys) {
      var _this6 = this;
      return new View(this.parent, indices.map(function (index) {
        return _this6.indices[index];
      }), keys);
    }
  }]);
  return View;
}();
/**
 * A DataSet subclass that can be constructed from a {@link Parsed} object
 */
var Savvy = /*#__PURE__*/function () {
  /**
   *
   * @param parsed a {@link Parsed} object generated with a {@link SavParser}
   */
  function Savvy(parsed) {
    _classCallCheck(this, Savvy);
    var _a;
    this.cases = parsed.meta.cases;
    this._names = parsed.internal.names;
    this.data = parsed.rows;
    var levels = new Map(parsed.headers.map(function (header) {
      return [header.name, new Map()];
    }));
    var cursor = 0;
    var indexmap = new Map(parsed.headers.map(function (header, idx) {
      var offset = cursor + 1;
      cursor++;
      cursor += header.trailers;
      return [offset, idx];
    }));
    parsed.internal.levels.forEach(function (entry) {
      return entry.indices.forEach(function (index) {
        return indexmap.has(index) && levels.set(parsed.headers[indexmap.get(index)].name, entry.map);
      });
    });
    this.fields = new Map();
    this.overflows = new Map();
    this._labels = new Map();
    var j = 0;
    for (var i = 0; i < parsed.headers.length; i++) {
      j = i;
      var header = parsed.headers[i];
      this._labels.set(header.name, header.label);
      if (header.code) {
        var overflow = [];
        if (parsed.internal.longs.has(header.name)) {
          var segs = Math.floor(parsed.internal.longs.get(header.name) / 252);
          while (segs > 0) {
            segs -= 1;
            overflow.push(parsed.headers[++i].name);
          }
        }
        this.overflows.set(header.name, overflow);
        this.fields.set(header.name, new StrColumn(this, header.name, new Set(header.missing.strings)));
      } else {
        if ((_a = levels.get(header.name)) === null || _a === void 0 ? void 0 : _a.size) {
          this.fields.set(header.name, new FacColumn(this, header.name, levels.get(header.name), new Set(header.missing.codes), parsed.internal.display[j].type));
        } else {
          this.fields.set(header.name, new NumColumn(this, header.name, new Set(header.missing.codes), header.missing.range, parsed.internal.display[j].type));
        }
      }
    }
  }
  _createClass(Savvy, [{
    key: "n",
    get: function get() {
      return this.cases;
    }
  }, {
    key: "keys",
    get: function get() {
      return Array.from(this.fields.keys());
    }
    /**
     * A map of of unique column keys to variable names
     */
  }, {
    key: "names",
    get: function get() {
      return new Map(_toConsumableArray(this._names));
    },
    set: function set(names) {
      var _this7 = this;
      names.forEach(function (value, key) {
        if (_this7._names.has(key)) {
          _this7._names.set(key, value);
        }
      });
    }
    /**
     * A map of of unique column keys to longer labels
     */
  }, {
    key: "labels",
    get: function get() {
      return new Map(_toConsumableArray(this._labels));
    },
    set: function set(labels) {
      var _this8 = this;
      labels.forEach(function (value, key) {
        if (_this8._labels.has(key)) {
          _this8._labels.set(key, value);
        }
      });
    }
  }, {
    key: "row",
    value: function row(index) {
      var _this9 = this;
      var cast = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : true;
      var row = new Map();
      this.keys.forEach(function (key) {
        return row.set(key, _this9.cell(index, key, cast));
      });
      return row;
    }
  }, {
    key: "field",
    value: function field(key) {
      var _a;
      return (_a = this.fields.get(key)) !== null && _a !== void 0 ? _a : new NullColumn(this);
    }
  }, {
    key: "col",
    value: function col(key) {
      var _this10 = this;
      var cast = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : true;
      return new Array(this.n).fill(0).map(function (_, idx) {
        return _this10.cell(idx, key, cast);
      });
    }
  }, {
    key: "cell",
    value: function cell(index, key) {
      var cast = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : true;
      var _a;
      var field = this.field(key);
      var row = this.data[index];
      var raw = row.get(key);
      (_a = this.overflows.get(key)) === null || _a === void 0 ? void 0 : _a.forEach(function (overflow) {
        var _a;
        raw = raw.toString() + ((_a = row.get(overflow)) !== null && _a !== void 0 ? _a : '');
      });
      return cast ? field.cast(raw) : raw;
    }
  }, {
    key: "view",
    value: function view(indices, fields) {
      return new View(this, indices, fields);
    }
  }]);
  return Savvy;
}();
exports.Savvy = Savvy;

/***/ })
/******/ 	]);
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
(() => {
var exports = __webpack_exports__;


function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); enumerableOnly && (symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; })), keys.push.apply(keys, symbols); } return keys; }
function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = null != arguments[i] ? arguments[i] : {}; i % 2 ? ownKeys(Object(source), !0).forEach(function (key) { _defineProperty(target, key, source[key]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)) : ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } return target; }
function _defineProperty(obj, key, value) { key = _toPropertyKey(key); if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }
function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread(); }
function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }
function _iterableToArray(iter) { if (typeof Symbol !== "undefined" && iter[Symbol.iterator] != null || iter["@@iterator"] != null) return Array.from(iter); }
function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) return _arrayLikeToArray(arr); }
function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _unsupportedIterableToArray(arr, i) || _nonIterableRest(); }
function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) arr2[i] = arr[i]; return arr2; }
function _iterableToArrayLimit(arr, i) { var _i = null == arr ? null : "undefined" != typeof Symbol && arr[Symbol.iterator] || arr["@@iterator"]; if (null != _i) { var _s, _e, _x, _r, _arr = [], _n = !0, _d = !1; try { if (_x = (_i = _i.call(arr)).next, 0 === i) { if (Object(_i) !== _i) return; _n = !1; } else for (; !(_n = (_s = _x.call(_i)).done) && (_arr.push(_s.value), _arr.length !== i); _n = !0); } catch (err) { _d = !0, _e = err; } finally { try { if (!_n && null != _i["return"] && (_r = _i["return"](), Object(_r) !== _r)) return; } finally { if (_d) throw _e; } } return _arr; } }
function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(arg) { var key = _toPrimitive(arg, "string"); return _typeof(key) === "symbol" ? key : String(key); }
function _toPrimitive(input, hint) { if (_typeof(input) !== "object" || input === null) return input; var prim = input[Symbol.toPrimitive]; if (prim !== undefined) { var res = prim.call(input, hint || "default"); if (_typeof(res) !== "object") return res; throw new TypeError("@@toPrimitive must return a primitive value."); } return (hint === "string" ? String : Number)(input); }
Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Savvy = exports.SavParser = exports.Feeder = void 0;
/**
 * An object that stores an {@link ArrayBuffer} and returns subsequent portions on demand
 */
var Feeder = /*#__PURE__*/function () {
  /**
   *
   * @param buffer An {@link ArrayBuffer} that will be fed out by the object
   */
  function Feeder(buffer) {
    _classCallCheck(this, Feeder);
    this.buffer = buffer;
    this.cursor = 0;
  }
  /**
   * Jump the cursor to a position in the buffer.
   * @param position the position in the {@link ArrayBuffer} to jump to
   */
  _createClass(Feeder, [{
    key: "jump",
    value: function jump(position) {
      if (position < 0 || position > this.buffer.byteLength) {
        throw new Error('Jump to out-of-bounds position');
      }
      this.cursor = position;
    }
    /**
     * Get the next chunk of the ArrayBuffer from the current cursor position
     * and move the cursor.
     * @param size the number of bytes to read from the {@link ArrayBuffer}
     * @returns an {@link ArrayBuffer} of the requested `size` from the cursor position
     */
  }, {
    key: "next",
    value: function next(size) {
      if (!this.buffer || this.cursor + size > this.buffer.byteLength) {
        throw new Error('Unexpected End of File');
      } else {
        this.cursor += size;
        return this.buffer.slice(this.cursor - size, this.cursor);
      }
    }
    /**
     * Get the current position of the cursor
     * @returns the current cursor position as a number
     */
  }, {
    key: "position",
    value: function position() {
      return this.cursor;
    }
    /**
     * Check whether the {@link ArrayBuffer} has been exhausted
     * @returns a boolean, whether the {@link ArrayBuffer} is exhausted
     */
  }, {
    key: "done",
    value: function done() {
      return this.cursor === this.buffer.byteLength;
    }
  }]);
  return Feeder;
}();
exports.Feeder = Feeder;
var DataReader = /*#__PURE__*/function () {
  function DataReader(schema, feeder) {
    var log = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : [];
    _classCallCheck(this, DataReader);
    this.feeder = feeder;
    this.position = feeder.position();
    this.cursor = 8;
    this.schema = schema;
    this.decoder = new TextDecoder();
    this.log = log;
  }
  _createClass(DataReader, [{
    key: "compressedCodes",
    value: function compressedCodes() {
      var instruction;
      do {
        if (this.cursor > 7) {
          this.instructions = new DataView(this.feeder.next(8));
          this.cursor = 0;
        }
        instruction = this.instructions.getUint8(this.cursor++);
      } while (instruction === 0);
      return instruction;
    }
  }, {
    key: "uncompressedNumber",
    value: function uncompressedNumber() {
      return new DataView(this.feeder.next(8)).getFloat64(0, this.schema.internal.integer.endianness === 2);
    }
  }, {
    key: "uncompressedString",
    value: function uncompressedString(length) {
      var pieces = [];
      do {
        pieces.concat(this.decoder.decode(this.feeder.next(8)));
      } while (--length);
      return pieces.join('');
    }
  }, {
    key: "compressedNumber",
    value: function compressedNumber() {
      var code = this.compressedCodes();
      switch (code) {
        case 252:
          throw new Error('Unexpected end of records.');
        case 253:
          return new DataView(this.feeder.next(8)).getFloat64(0, true);
        case 254:
          throw new Error('Cell code type mismatch');
        case 255:
          return null;
        default:
          return code - this.schema.meta.bias;
      }
    }
  }, {
    key: "compressedString",
    value: function compressedString(length) {
      var pieces = [];
      do {
        var code = this.compressedCodes();
        switch (code) {
          case 252:
            throw new Error('Unexpected end of records.');
          case 253:
            pieces.push(this.decoder.decode(this.feeder.next(8)));
            break;
          case 254:
            pieces.push('');
            break;
          case 255:
            return null;
          default:
            throw new Error('Default code not supported for strings.');
        }
      } while (--length);
      return pieces.join('');
    }
  }, {
    key: "readNumber",
    value: function readNumber() {
      if (this.schema.meta.compression) {
        return this.compressedNumber();
      } else {
        return this.uncompressedNumber();
      }
    }
  }, {
    key: "readString",
    value: function readString(length) {
      if (this.schema.meta.compression) {
        return this.compressedString(length);
      } else {
        return this.uncompressedString(length);
      }
    }
  }, {
    key: "readCell",
    value: function readCell(header) {
      this.log.push('Cell: ' + header.name);
      if (header.code) {
        return this.readString(Math.ceil(header.code / 8));
      } else {
        return this.readNumber();
      }
    }
  }, {
    key: "readRow",
    value: function readRow() {
      var _this = this;
      return new Map(this.schema.headers.map(function (header) {
        return [header.name, _this.readCell(header)];
      }));
    }
  }, {
    key: "read",
    value: function read() {
      var _this2 = this;
      this.feeder.jump(this.schema.internal.finished);
      var readArray = new Array(this.schema.meta.cases).fill(0).map(function (_, idx) {
        _this2.log.push('Row: ' + idx);
        return _this2.readRow();
      });
      this.feeder.jump(this.position);
      return readArray;
    }
  }]);
  return DataReader;
}();
/**
 * A parser for .sav files
 */
var SavParser = /*#__PURE__*/function () {
  /**
   * Create a new parser
   * @param log a string array that will be populated by parse calls
   */
  function SavParser() {
    var log = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : [];
    _classCallCheck(this, SavParser);
    this.decoder = new TextDecoder();
    this.log = log;
  }
  _createClass(SavParser, [{
    key: "readFieldLabel",
    value: function readFieldLabel(feeder) {
      var length = new DataView(feeder.next(4)).getInt32(0, true);
      if (length % 4) {
        length = length + (4 - length % 4);
      }
      return this.decoder.decode(feeder.next(length)).trim();
    }
  }, {
    key: "readFieldMissingCodes",
    value: function readFieldMissingCodes(view, count) {
      var readArray = new Array(count).fill(0);
      return readArray.map(function (_, idx) {
        return view.getFloat64(8 * idx);
      });
    }
  }, {
    key: "readFieldMissingStrings",
    value: function readFieldMissingStrings(chunk, count) {
      var _this3 = this;
      var readArray = new Array(count).fill(0);
      return readArray.map(function (_, idx) {
        return _this3.decoder.decode(chunk.slice(8 * idx, 8 * idx + 8));
      });
    }
  }, {
    key: "readFieldMissingRange",
    value: function readFieldMissingRange(view) {
      return [view.getFloat64(0, true), view.getFloat64(8, true)];
    }
  }, {
    key: "readFieldMissing",
    value: function readFieldMissing(feeder, numeric, code) {
      var chunk = feeder.next(8 * Math.abs(code));
      var view = new DataView(chunk);
      return {
        codes: numeric && code > 0 ? this.readFieldMissingCodes(view, code) : numeric && code === -3 ? this.readFieldMissingCodes(view, 3).slice(2) : [],
        range: numeric && code < 0 ? this.readFieldMissingRange(view) : [undefined, undefined],
        strings: !numeric && code > 0 ? this.readFieldMissingStrings(chunk, code) : []
      };
    }
  }, {
    key: "readField",
    value: function readField(feeder) {
      this.log.push('Reading Field at ' + feeder.position());
      var start = feeder.position();
      var chunk = feeder.next(28);
      var view = new DataView(chunk);
      var code = view.getInt32(0, true);
      var labeled = view.getInt32(4, true);
      var missings = view.getInt32(8, true);
      var name = this.decoder.decode(chunk.slice(20, 28)).trim();
      var label = labeled ? this.readFieldLabel(feeder) : '';
      var missing = missings ? this.readFieldMissing(feeder, code === 0, missings) : {
        codes: [],
        range: [undefined, undefined],
        strings: []
      };
      return {
        start: start,
        code: code,
        name: name,
        label: label,
        missing: missing,
        trailers: 0
      };
    }
  }, {
    key: "getLevel",
    value: function getLevel(feeder) {
      this.log.push('Scale level at ' + feeder.position());
      var view = new DataView(feeder.next(9));
      var length = view.getInt8(8);
      var size = (length + 1) % 8 ? length + (8 - (length + 1) % 8) : length;
      return [view.getFloat64(0, true), this.decoder.decode(feeder.next(size)).substring(0, length).trim()];
    }
  }, {
    key: "readScale",
    value: function readScale(feeder) {
      var _this4 = this;
      this.log.push('Scale definition at ' + feeder.position());
      var count = new DataView(feeder.next(4)).getInt32(0, true);
      var readArray = new Array(count).fill(0);
      var levels = new Map(readArray.map(function () {
        return _this4.getLevel(feeder);
      }));
      var view = new DataView(feeder.next(8));
      var magic = view.getInt32(0, true);
      var icount = view.getInt32(4, true);
      if (magic !== 4) {
        throw new Error('Levels read error. ' + 'Magic value Expected: 4 ' + 'Actual: ' + magic);
      }
      var iview = new DataView(feeder.next(4 * icount));
      var indices = new Set(new Array(icount).fill(0).map(function (_, idx) {
        return iview.getInt32(idx * 4, true);
      }));
      return {
        map: levels,
        indices: indices
      };
    }
  }, {
    key: "readDocument",
    value: function readDocument(feeder) {
      var _this5 = this;
      this.log.push('Sys Document at ' + feeder.position());
      var count = new DataView(feeder.next(4)).getInt32(0, true);
      var chunk = feeder.next(count * 80);
      var docArray = new Array(count).fill(0);
      return docArray.map(function (_, idx) {
        return _this5.decoder.decode(chunk.slice(idx * 80, idx * 80 + 80));
      });
    }
  }, {
    key: "readSysInteger",
    value: function readSysInteger(feeder) {
      this.log.push('Sys Integer at ' + feeder.position());
      var view = new DataView(feeder.next(32));
      return {
        major: view.getInt32(0, true),
        minor: view.getInt32(4, true),
        revision: view.getInt32(8, true),
        machine: view.getInt32(12, true),
        "float": view.getInt32(16, true),
        compression: view.getInt32(20, true),
        endianness: view.getInt32(24, true),
        character: view.getInt32(28, true)
      };
    }
  }, {
    key: "readSysFloat",
    value: function readSysFloat(feeder) {
      this.log.push('Sys Float at ' + feeder.position());
      var view = new DataView(feeder.next(24));
      return {
        missing: view.getFloat64(0, true),
        high: view.getFloat64(8, true),
        low: view.getFloat64(16, true)
      };
    }
  }, {
    key: "readSysDisplay",
    value: function readSysDisplay(feeder, count) {
      this.log.push('Sys Display at ' + feeder.position());
      var view = new DataView(feeder.next(count * 12));
      var dispArray = new Array(count).fill(0);
      return dispArray.map(function (_, idx) {
        return {
          type: view.getInt32(idx * 12, true),
          width: view.getInt32(idx * 12 + 4, true),
          align: view.getInt32(idx * 12 + 8, true)
        };
      });
    }
  }, {
    key: "readNames",
    value: function readNames(feeder, size) {
      this.log.push('Names at ' + feeder.position());
      var raw = this.decoder.decode(feeder.next(size));
      return new Map(raw.split('\t').map(function (str) {
        return str.split('=');
      }));
    }
  }, {
    key: "readLongWidths",
    value: function readLongWidths(feeder, size) {
      this.log.push('Long Widths at ' + feeder.position());
      var raw = this.decoder.decode(feeder.next(size));
      var rows = raw.split('\t');
      return new Map(rows.slice(0, rows.length - 1).map(function (str) {
        return str.split('=');
      }).map(function (_ref) {
        var _ref2 = _slicedToArray(_ref, 2),
          name = _ref2[0],
          length = _ref2[1];
        return [name, parseInt(length, 10)];
      }));
    }
  }, {
    key: "readLongNames",
    value: function readLongNames(feeder, size) {
      this.log.push('Long Names at ' + feeder.position());
      // need to figure out how this works
      return feeder.next(size);
    }
  }, {
    key: "readUnrecognized",
    value: function readUnrecognized(feeder, count, length) {
      var chunk = feeder.next(count * length);
      var readArray = new Array(count).fill(0);
      return readArray.map(function (_, idx) {
        return chunk.slice(idx * length, idx * length + length);
      });
    }
  }, {
    key: "readInternal",
    value: function readInternal(feeder) {
      var _a, _b, _c, _d, _e, _f, _g, _h, _j, _k, _l, _m, _o, _p, _q, _r;
      this.log.push('Reading Internal');
      var partial = {};
      var code;
      var subcode;
      var subview;
      var length;
      var count;
      while (!partial.finished) {
        code = new DataView(feeder.next(4)).getInt32(0, true);
        switch (code) {
          case 3:
            partial.levels = ((_a = partial.levels) !== null && _a !== void 0 ? _a : []).concat(this.readScale(feeder));
            break;
          case 6:
            partial.documents = ((_b = partial.documents) !== null && _b !== void 0 ? _b : []).concat(this.readDocument(feeder));
            break;
          case 7:
            subview = new DataView(feeder.next(12));
            subcode = subview.getInt32(0, true);
            length = subview.getInt32(4, true);
            count = subview.getInt32(8, true);
            switch (subcode) {
              case 3:
                this.log.push('Subcode 3');
                if (length * count !== 32) {
                  throw new Error('Special code 3 ' + 'Expected: 32 bytes; ' + 'Actual: ' + length * count);
                }
                partial.integer = this.readSysInteger(feeder);
                break;
              case 4:
                this.log.push('Subcode 4');
                if (length * count !== 24) {
                  throw new Error('Special code 4 ' + 'Expected: 24 bytes; ' + 'Actual: ' + length * count);
                }
                partial["float"] = this.readSysFloat(feeder);
                break;
              case 11:
                this.log.push('Subcode 11');
                if (length !== 4) {
                  throw new Error('Special code 11 ' + 'Expected: 4 bytes; ' + 'Actual: ' + length);
                }
                if (count % 3) {
                  throw new Error('Special code 11 ' + 'Expected: Length factor of 3; ' + 'Actual: ' + length);
                }
                partial.display = ((_c = partial.display) !== null && _c !== void 0 ? _c : []).concat(this.readSysDisplay(feeder, count / 3));
                break;
              case 13:
                this.log.push('Subcode 13');
                partial.names = new Map([].concat(_toConsumableArray((_d = partial.names) !== null && _d !== void 0 ? _d : []), _toConsumableArray(this.readNames(feeder, count * length))));
                break;
              case 14:
                this.log.push('Subcode 14');
                partial.longs = new Map([].concat(_toConsumableArray((_e = partial.longs) !== null && _e !== void 0 ? _e : []), _toConsumableArray(this.readLongWidths(feeder, count * length))));
                break;
              case 21:
                this.log.push('Subcode 21');
                partial.extra = ((_f = partial.extra) !== null && _f !== void 0 ? _f : []).concat(this.readLongNames(feeder, count * length));
                break;
              default:
                this.log.push('Unrecognized Subcode');
                partial.unrecognized = ((_g = partial.unrecognized) !== null && _g !== void 0 ? _g : []).concat([[subcode, this.readUnrecognized(feeder, count, length)]]);
                break;
            }
            break;
          case 999:
            feeder.next(4);
            partial.finished = feeder.position();
            break;
          default:
            throw new Error('Internal Code Expected : [3, 6, 7, 999]; Actual : ' + code);
        }
      }
      return {
        "float": (_h = partial["float"]) !== null && _h !== void 0 ? _h : {
          missing: undefined,
          high: undefined,
          low: undefined
        },
        integer: (_j = partial.integer) !== null && _j !== void 0 ? _j : {
          major: undefined,
          minor: undefined,
          revision: undefined,
          machine: undefined,
          "float": undefined,
          compression: undefined,
          endianness: undefined,
          character: undefined
        },
        display: (_k = partial.display) !== null && _k !== void 0 ? _k : [],
        documents: (_l = partial.documents) !== null && _l !== void 0 ? _l : [],
        names: (_m = partial.names) !== null && _m !== void 0 ? _m : new Map(),
        longs: (_o = partial.longs) !== null && _o !== void 0 ? _o : new Map(),
        levels: (_p = partial.levels) !== null && _p !== void 0 ? _p : [],
        extra: (_q = partial.extra) !== null && _q !== void 0 ? _q : [],
        unrecognized: (_r = partial.unrecognized) !== null && _r !== void 0 ? _r : [],
        finished: partial.finished
      };
    }
  }, {
    key: "readFields",
    value: function readFields(feeder) {
      this.log.push('Reading Field at ' + feeder.position());
      var code;
      var fields = [];
      var field;
      while (true) {
        code = new DataView(feeder.next(4)).getInt32(0, true);
        if (code !== 2) {
          feeder.jump(feeder.position() - 4);
          break;
        }
        field = this.readField(feeder);
        if (field.code > -1) {
          fields.push(field);
        } else {
          fields[fields.length - 1].trailers++;
        }
      }
      return fields;
    }
    /**
     * Read the meta fields from a .sav file
     * @param feeder A {@link Feeder} object encoding the sav file
     * @remarks
     * From a node.js {@link Buffer} using `fs.readFile`
     * ```
     * fs = require('fs');
     *
     * let meta;
     * const parser = new SavParser()
     * // with async readFile
     * fs.readFile('some/path/to/file.sav', (err, data) => {
     *     parser.meta(new Feeder(data.buffer)).then(
     *         result => meta = result
     *     )
     * });
     * // with syncronous readFileSync
     * parser.meta(
     *     new Feeder(fs.readFileSync('/some/path/to/file.sav').buffer)
     * ).then(
     *     parsed => meta = parsed
     * );
     * ```
     *
     * In the browser with a File API
     * ```
     *     <input type="file" onchange = "onChange(event)"></input>
     * ```
     * ```
     * const meta;
     * function onChange(event){
     *     const file = event.target.files[0];
     *     const reader = new FileReader();
     *     const parser = new SavParser();
     *     reader.onload = function(data){
     *         data.arrayBuffer().then(
     *             buffer => parser.meta(new Feeder(buffer))
     *         ).then(
     *             parsed => meta = parsed
     *         );
     *     }
     *     reader.readAsArrayBuffer(file);
     * }
     * ```
     * @return A promise resolving with a {@link Meta} object
     */
  }, {
    key: "meta",
    value: function meta(feeder) {
      var _this6 = this;
      this.log.splice(0, this.log.length);
      var position = feeder.position();
      feeder.jump(0);
      return new Promise(function (resolve, reject) {
        var chunk = feeder.next(176);
        var view = new DataView(chunk);
        var magic = _this6.decoder.decode(chunk.slice(0, 4));
        if (magic !== '$FL2') {
          reject(new Error('File is not a sav. ' + 'Magic key Expected: "$FL2"; ' + 'Actual: ' + magic));
        }
        resolve({
          product: _this6.decoder.decode(chunk.slice(4, 64)).trim(),
          layout: view.getInt32(64, true),
          variables: view.getInt32(68, true),
          compression: view.getInt32(72, true),
          weightIndex: view.getInt32(76, true),
          cases: view.getInt32(80, true),
          bias: view.getFloat64(84, true),
          createdDate: _this6.decoder.decode(chunk.slice(92, 101)),
          createdTime: _this6.decoder.decode(chunk.slice(101, 109)),
          label: _this6.decoder.decode(chunk.slice(109, 173)).trim()
        });
      })["finally"](function () {
        return feeder.jump(position);
      });
    }
    /**
     * Read the column header fields from a .sav file.
     * Header here refers to the head of the columns of the data, i.e.
     * properties of the variables in the data file
     * @param feeder A {@link Feeder} object encoding the sav file
     * @remarks
     * From a node.js {@link Buffer} using `fs.readFile`
     * ```
     * fs = require('fs');
     *
     * let headers;
     * const parser = new SavParser()
     * // with async readFile
     * fs.readFile('some/path/to/file.sav', (err, data) => {
     *     parser.headers(new Feeder(data.buffer)).then(
     *         result => headers = result
     *     )
     * });
     * // with syncronous readFileSync
     * parser.headers(
     *     new Feeder(fs.readFileSync('/some/path/to/file.sav').buffer)
     * ).then(
     *     parsed => headers = parsed
     * );
     * ```
     *
     * In the browser with a File API
     * ```
     *     <input type="file" onchange = "onChange(event)"></input>
     * ```
     * ```
     * const headers;
     * function onChange(event){
     *     const file = event.target.files[0];
     *     const reader = new FileReader();
     *     const parser = new SavParser();
     *     reader.onload = function(data){
     *         data.arrayBuffer().then(
     *             buffer => parser.headers(new Feeder(buffer))
     *         ).then(
     *             parsed => headers = parsed
     *         );
     *     }
     *     reader.readAsArrayBuffer(file);
     * }
     * ```
     * @return A promise resolving with an Array<{@link Meta}> object
     */
  }, {
    key: "headers",
    value: function headers(feeder) {
      this.log.splice(0, this.log.length);
      var position = feeder.position();
      feeder.jump(176);
      return Promise.resolve(this.readFields(feeder))["finally"](function () {
        return feeder.jump(position);
      });
    }
    /**
     * Read all schema fields from a .sav file.
     * Schema here refers to all information except for the data cells themselves
     * @param feeder A {@link Feeder} object encoding the sav file
     * @remarks
     * From a node.js {@link Buffer} using `fs.readFile`
     * ```
     * fs = require('fs');
     *
     * let schema;
     * const parser = new SavParser()
     * // with async readFile
     * fs.readFile('some/path/to/file.sav', (err, data) => {
     *     parser.schema(new Feeder(data.buffer)).then(
     *         result => schema = result
     *     )
     * });
     * // with syncronous readFileSync
     * parser.schema(
     *     new Feeder(fs.readFileSync('/some/path/to/file.sav').buffer)
     * ).then(
     *     parsed => schema = parsed
     * );
     * ```
     *
     * In the browser with a File API
     * ```
     *     <input type="file" onchange = "onChange(event)"></input>
     * ```
     * ```
     * const schema;
     * function onChange(event){
     *     const file = event.target.files[0];
     *     const reader = new FileReader();
     *     const parser = new SavParser();
     *     reader.onload = function(data){
     *         data.arrayBuffer().then(
     *             buffer => parser.schema(new Feeder(buffer))
     *         ).then(
     *             parsed => schema = parsed
     *         );
     *     }
     *     reader.readAsArrayBuffer(file);
     * }
     * ```
     * @return A promise resolving with an {@link Schema} object
     */
  }, {
    key: "schema",
    value: function schema(feeder) {
      var _this7 = this;
      this.log.splice(0, this.log.length);
      var position = feeder.position();
      return this.meta(feeder).then(function (meta) {
        return {
          meta: meta
        };
      }).then(function (partial) {
        feeder.jump(176);
        return _objectSpread(_objectSpread({}, partial), {}, {
          headers: _this7.readFields(feeder)
        });
      }).then(function (partial) {
        return _objectSpread(_objectSpread({}, partial), {}, {
          internal: _this7.readInternal(feeder)
        });
      })["finally"](function () {
        return feeder.jump(position);
      });
    }
    /**
     * Read all fields from a .sav file.
     * All fields include the full {@link Schema} and all data cells as an
     * Array<{@link Row}.
     * @param feeder A {@link Feeder} object encoding the sav file
     * @remarks
     * From a node.js {@link Buffer} using `fs.readFile`
     * ```
     * fs = require('fs');
     *
     * let all;
     * const parser = new SavParser()
     * // with async readFile
     * fs.readFile('some/path/to/file.sav', (err, data) => {
     *     parser.all(new Feeder(data.buffer)).then(
     *         result => all = result
     *     )
     * });
     * // with syncronous readFileSync
     * parser.all(
     *     new Feeder(fs.readFileSync('/some/path/to/file.sav').buffer)
     * ).then(
     *     parsed => all = parsed
     * );
     * ```
     *
     * In the browser with a File API
     * ```
     *     <input type="file" onchange = "onChange(event)"></input>
     * ```
     * ```
     * const all;
     * function onChange(event){
     *     const file = event.target.files[0];
     *     const reader = new FileReader();
     *     const parser = new SavParser();
     *     reader.onload = function(data){
     *         data.arrayBuffer().then(
     *             buffer => parser.all(new Feeder(buffer))
     *         ).then(
     *             parsed => all = parsed
     *         );
     *     }
     *     reader.readAsArrayBuffer(file);
     * }
     * ```
     * @return A promise resolving with an {@link Parsed} object
     */
  }, {
    key: "all",
    value: function all(feeder) {
      var _this8 = this;
      this.log.splice(0, this.log.length);
      var position = feeder.position();
      return this.schema(feeder).then(function (schema) {
        return _objectSpread(_objectSpread({}, schema), {}, {
          rows: new DataReader(schema, feeder, _this8.log).read()
        });
      })["finally"](function () {
        return feeder.jump(position);
      });
    }
  }]);
  return SavParser;
}();
exports.SavParser = SavParser;
var dataset_1 = __webpack_require__(1);
Object.defineProperty(exports, "Savvy", ({
  enumerable: true,
  get: function get() {
    return dataset_1.Savvy;
  }
}));
})();

/******/ 	return __webpack_exports__;
/******/ })()
;
});
//# sourceMappingURL=index.js.map