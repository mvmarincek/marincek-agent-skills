import sys, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from route_skills import rank  # noqa: E402


class RouterRankingTests(unittest.TestCase):
    """Regressao do roteador: cenarios da Legacy Rule V5/v5.1.

    Landing com montagem 3D sem sinais de fabrica real deve liderar com
    immersive-commerce-3d; gemeos de fabricacao exigem sinais fortes
    (MES/ERP/VIN/fabrica/producao), nao apenas 'montagem 3D'.
    """

    def _top(self, task, n=3):
        return [c['skill'] for c in rank(task, top=n)]

    def test_landing_3d_gamificada_leads_with_immersive_commerce(self):
        top = self._top('landing page gamificada com montagem 3D de produto jogavel')
        self.assertEqual(top[0], 'immersive-commerce-3d')
        self.assertNotIn('made-to-order-manufacturing-twin', top)

    def test_manufacturing_twin_requires_factory_signals(self):
        # 'montagem 3D' isolado NAO dispara o bonus de fabricacao (+55):
        # a skill pode aparecer por match lexico fraco, mas sem liderar
        results = rank('montagem 3D do produto na tela', top=5)
        twin = next((r for r in results if r['skill'] == 'made-to-order-manufacturing-twin'), None)
        if twin is not None:
            self.assertLess(twin['score'], 20, 'bonus de fabricacao disparou sem sinais fortes (MES/ERP/VIN/fabrica)')

    def test_factory_query_leads_with_manufacturing_twin(self):
        top = self._top('carro configurado 3D montando na fabrica MES ERP VIN')
        self.assertEqual(top[0], 'made-to-order-manufacturing-twin')

    def test_live_kitchen_ops_leads_with_realworld_twin(self):
        top = self._top('acompanhar pedido real da cozinha no KDS em tempo real')
        self.assertEqual(top[0], 'realworld-order-digital-twin')

    def test_ci_failure_leads_with_ci_fix_loop(self):
        top = self._top('pipeline CI vermelho checks falhando no pull request')
        self.assertEqual(top[0], 'ci-fix-loop')


if __name__ == '__main__':
    unittest.main()
