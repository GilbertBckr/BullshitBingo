<script setup></script>
<script>
import { joinGame } from "@/logic/token";

export default {
    methods: {
        show() {
            this.$refs.dialog.show();
        },

        hide() {
            this.$refs.dialog.close();
        },
    },
};
</script>

<template>
    <md-dialog ref="dialog" lang="de">
        <div slot="headline">Imprint</div>
        <div slot="content">
            <p>Angaben gemäß &sect; 5 TMG: <br>
                Mathis Köder <br>
                Erzbergerstraße 121 <br>
                76133 Karlsruhe <br>
                015128867198 <br>

                Mathis.koeder.a23@dhbw-karlsruhe.de <br>
                Umsatzsteuer-ID: - <br>
                Umsatzsteuer-Identifikationsnummer gemäß &sect; 27 a Umsatzsteuergesetz: - <br><br>
                <strong>Haftung für Inhalte</strong> <br>
                Die Inhalte unserer Webseite wurden mit größtmöglicher Sorgfalt erstellt. Für die Richtigkeit,
                Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen. Als
                Diensteanbieter sind wir gemäß &sect; 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen
                Gesetzen verantwortlich. Nach &sect; 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht verpflichtet,
                übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen,
                die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der
                Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt.
                Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten
                Rechtsverletzung möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen werden wir diese
                Inhalte umgehend entfernen.
                <br><br><strong>Urheberrecht</strong> <br>
                Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen
                Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der
                Grenzen des Urheberrechts bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.
                Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet.
                Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden die Urheberrechte
                Dritter beachtet. Insbesondere werden Inhalte Dritter als solche gekennzeichnet. Sollten Sie trotzdem
                auf eine Urheberrechtsverletzung aufmerksam werden, bitten wir um einen entsprechenden Hinweis. Bei
                Bekanntwerden von Rechtsverletzungen werden wir derartige Inhalte umgehend entfernen.
            </p>
        </div>
        <div slot="actions">
            <md-text-button value="cancel" ref="buttonCancel" @click="hide">Close</md-text-button>
        </div>
    </md-dialog>
</template>

<style scoped></style>
