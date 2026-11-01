# Máquina de estados: pickup → transporte → depósito

```text
idle --pick(id)--> selected --raycast_ok--> reaching --contact--> grasping
  --item_attached--> carrying --target_valid--> placing --release--> committed --> idle
                qualquer estado --cancel/error--> rollback --> idle
```

## Invariantes
- Uma e somente uma `activeAction` por mão. Não aceitar `pick` durante `carrying`.
- `itemUnderHand` tem um `instanceId` único; ao colocar, novo mesh recebe `instanceId` e coords locais da superfície.
- Todos os ingredientes commitados aparecem em `SceneGraph` e em `ProductState` ao mesmo tempo.
- O 3D não determina o preço final: checkout com precificação autoritativa.
- Ao desfazer, remover apenas o último commit e recalcular subtotal; undo é vedado depois da confirmação do pedido sem política real.

## Cenas de teste
A) morango seguido de banana; B) dois cliques rápidos; C) tentativa de depositar fora da massa; D) perder WebGL durante carry; E) desfazer; F) troca de câmera; G) toque em mobile.

## Pseudocódigo
```ts
// representação, não código de produção
function commitDrop(action, placement) {
  assert(action.stage === 'placing' && withinCrepe(placement));
  state.ingredients.push({instanceId: action.id, ingredientId: action.ingredientId, transform: placement});
  scene.attachIngredientMesh(action.id, placement);
  events.emit('ingredient_committed', {ingredientId: action.ingredientId, instanceId: action.id});
}
```
