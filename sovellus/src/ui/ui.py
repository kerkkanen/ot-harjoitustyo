from ui.score_view import ScoreView
from ui.start_view import StartView
from ui.ready_view import ReadyView
from ui.game_view import GameView
from ui.score_view import ScoreView


class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._show_ready_view,
            self._show_score_view
        )
        self._current_view.pack()

    def _show_ready_view(self, player_name, game_level, game_area):
        self._hide_current_view()

        self._current_view = ReadyView(
            self._root,
            self._show_start_view,
            self._show_game_view,
            player_name,
            game_level,
            game_area
        )
        self._current_view.pack()

    def _show_game_view(self, game):
        self._hide_current_view()

        self._current_view = GameView(
            self._root,
            self._show_score_view,
            game
        )
        self._current_view.pack()

    def _show_score_view(self, game):
        self._hide_current_view()

        self._current_view = ScoreView(
            self._root,
            self._show_start_view,
            game,
        )
        self._current_view.pack()
