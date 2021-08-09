# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

from telethon import TelegramClient
from telethon.sessions import StringSession

from AsunaRobot.conf import get_int_key, get_str_key

STRING_SESSION = get_str_key("STRING_SESSION", required=True)
API_ID = get_int_key("API_ID", required=True)
API_HASH = get_str_key("API_HASH", required=True)

ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
try:
    ubot.start()
except BaseException:
    print("Userbot Error ! Have you added a STRING_SESSION in deploying??")
    sys.exit(1)
