const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const source = fs.readFileSync(path.resolve(__dirname, '../../../05-Mockup/final-v4/app.js'), 'utf8');
const fn = source.slice(source.indexOf('async function loadFile('), source.indexOf('function printSpec('));
let finishDecode;
const state = { route: 'proof', image: null, proof: 'pending', fileVersion: 0 };
const main = {innerHTML: ''};
let bound = 0;
const context = vm.createContext({state, main, loadId: 0, resetProof:()=>{state.proof='pending';state.fileVersion++}, drawCheck:()=>{}, proof:()=>`proof:${state.proof}`, bind:()=>{bound++}, createImageBitmap:()=>new Promise(resolve=>{finishDecode=resolve})});
vm.runInContext(fn, context);
(async()=>{
  const pending = context.loadFile({type:'image/png',size:100,name:'new.png'});
  state.proof = 'approved'; // A decision made while decoding must not approve later artwork.
  finishDecode({width:2000,height:1200,close(){}});
  await pending;
  assert.equal(state.proof,'pending','decoded artwork invalidates any decision made while loading');
  assert.equal(main.innerHTML,'proof:pending','an open proof page is redrawn with the new artwork state');
  assert.equal(bound,1,'proof controls are rebound');
  console.log('PASS: asynchronous artwork decode resets and redraws the proof.');
})().catch(error=>{console.error(error.message);process.exitCode=1});
